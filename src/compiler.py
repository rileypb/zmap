from ctypes.wintypes import SMALL_RECT
from io import StringIO
import sys
from antlr4 import *  
from zmapLexer import zmapLexer
from zmapParser import zmapParser
from zmapListenerImpl import zmapListenerImpl

from map import *

from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QColor, QFont, QTextOption, QPolygonF, QBrush, QPen
from PyQt5.QtCore import Qt, QPointF

import math

TEXT_COLOR = QColor("black")
FONT = QFont("sans-serif", pointSize=10)
SMALL_FONT = QFont("sans-serif", pointSize=6)
TEXT_OPTION = QTextOption(Qt.AlignCenter)

ELLIPSE_SCALE = 1 / math.sqrt(2)
ARROWHEAD_SCALE = 5
ARROWHEAD_BRUSH = QBrush()
ARROWHEAD_BRUSH.setColor(QColor("black"))
ARROWHEAD_BRUSH.setStyle(Qt.SolidPattern)
DASH_PEN = QPen()
DASH_PEN.setDashPattern([5, 5])

opposites = { 'n': 's', 'ne': 'sw', 'e': 'w', 'se': 'nw', 's': 'n', 'sw': 'ne',
              'w': 'e', 'nw': 'se', 'u': 'd', 'd': 'u'}

def opposite(direction):
    return opposites[direction]

def attachment_point(subtype, room_rect, direction):
    if not subtype:
        if direction == 'n' or direction == 'u':
            return QPointF(room_rect.x() + room_rect.width() / 2, room_rect.y())
        elif direction == 'ne':
            return QPointF(room_rect.x() + room_rect.width(), room_rect.y())
        elif direction == 'e':
            return QPointF(room_rect.x() + room_rect.width(), room_rect.y() + room_rect.height() / 2)
        elif direction == 'se':
            return QPointF(room_rect.x() + room_rect.width(), room_rect.y() + room_rect.height())
        elif direction == 's' or direction == 'd':
            return QPointF(room_rect.x() + room_rect.width() / 2, room_rect.y() + room_rect.height())
        elif direction == 'sw':
            return QPointF(room_rect.x(), room_rect.y() + room_rect.height())
        elif direction == 'w':
            return QPointF(room_rect.x(), room_rect.y() + room_rect.height() / 2)
        elif direction == 'nw':
            return QPointF(room_rect.x(), room_rect.y())
        else: 
            raise RuntimeError("I don't understand direction: " + str(direction))

    elif subtype:
        center_x = room_rect.x() + room_rect.width() / 2
        center_y = room_rect.y() + room_rect.height() / 2
        if direction == 'n' or direction == 'u':
            return QPointF(center_x, room_rect.y())
        elif direction == 'ne':
            return QPointF(center_x + room_rect.width() / 2 * ELLIPSE_SCALE, center_y - room_rect.height() / 2 * ELLIPSE_SCALE)
        elif direction == 'e':
            return QPointF(room_rect.x() + room_rect.width(), center_y)
        elif direction == 'se':
            return QPointF(center_x + room_rect.width() / 2 * ELLIPSE_SCALE, center_y + room_rect.height() / 2 * ELLIPSE_SCALE)
        elif direction == 's' or direction == 'd':
            return QPointF(center_x, room_rect.y() + room_rect.height())
        elif direction == 'sw':
            return QPointF(center_x - room_rect.width() / 2 * ELLIPSE_SCALE, center_y + room_rect.height() / 2 * ELLIPSE_SCALE)
        elif direction == 'w':
            return QPointF(room_rect.x(), room_rect.y() + room_rect.height() / 2)
        elif direction == 'nw':
            return QPointF(center_x - room_rect.width() / 2 * ELLIPSE_SCALE, center_y - room_rect.height() / 2 * ELLIPSE_SCALE)
        else: 
            raise RuntimeError("I don't understand direction: " + str(direction))
    # elif subtype == 'Special':
    #     center_x = room_rect.x() + room_rect.width() / 2
    #     center_y = room_rect.y() + room_rect.height() / 2
    #     if direction == 'n' or direction == 'u':
    #         return QPointF(room_rect.x() + room_rect.width() / 2, room_rect.y())
    #     elif direction == 'ne':
    #         return QPointF(center_x + room_rect.width() / 4, center_y - room_rect.height() / 4)
    #     elif direction == 'e':
    #         return QPointF(room_rect.x() + room_rect.width(), room_rect.y() + room_rect.height() / 2)
    #     elif direction == 'se':
    #         return QPointF(center_x + room_rect.width() / 4, center_y + room_rect.height() / 4)
    #     elif direction == 's' or direction == 'd':
    #         return QPointF(room_rect.x() + room_rect.width() / 2, room_rect.y() + room_rect.height())
    #     elif direction == 'sw':
    #         return QPointF(center_x - room_rect.width() / 4, center_y + room_rect.height() / 4)
    #     elif direction == 'w':
    #         return QPointF(room_rect.x(), room_rect.y() + room_rect.height() / 2)
    #     elif direction == 'nw':
    #         return QPointF(center_x - room_rect.width() / 4, center_y - room_rect.height() / 4)
    #     else: 
    #         raise RuntimeError("I don't understand direction: " + str(direction))
        
def add_arrowhead(scene, to_point, from_point):
    point1 = to_point
    dx = from_point.x() - to_point.x()
    dy = from_point.y() - to_point.y()
    dist = math.sqrt(dx * dx + dy * dy)
    dx /= dist
    dy /= dist
    if dx == 0:
        dx = 0.01
    if dy == 0:
        dy = 0.01
    point_aux = QPointF(point1.x() + ARROWHEAD_SCALE * dx, point1.y() + ARROWHEAD_SCALE * dy)
    odx = ARROWHEAD_SCALE * dy / 2
    ody = ARROWHEAD_SCALE * -dx / 2
    point2 = QPointF(point_aux.x() + odx, point_aux.y() + ody)
    point3 = QPointF(point_aux.x() - odx, point_aux.y() - ody)
    polygon = QPolygonF()
    polygon.append(point1)
    polygon.append(point2)
    polygon.append(point3)
    scene.addPolygon(polygon, brush=ARROWHEAD_BRUSH)


class Compiler:
    def compile(self, source, scene):
        input_stream = InputStream(source)
        lexer = zmapLexer(input_stream)
        stream = CommonTokenStream(lexer)
        parser = zmapParser(stream)
        tree = parser.parse()
        listener = zmapListenerImpl()
        walker = ParseTreeWalker()
        walker.walk(listener, tree)
        listener.new_map.position_rooms()
        
        room_to_rect = {}

        for room in listener.new_map.rooms.values():
            x = 200+150*room.position[0]
            y = 200+150*room.position[1]
            text = scene.addText(room.label)
            text.setPos(x,-y)
            text.setDefaultTextColor(TEXT_COLOR)
            text.setFont(FONT)
            text.setTextWidth(50)
            text.document().setDefaultTextOption(TEXT_OPTION)
            if len(room.label) > 12:
                text.setFont(SMALL_FONT)
            text_bounding_rect = text.boundingRect()
            room.bounding_rect = QRectF(x - text_bounding_rect.width()/2, -y - text_bounding_rect.height()/2, max(50, text_bounding_rect.width()), text_bounding_rect.height())
            text.setPos(x - text_bounding_rect.width()/2, -y - text_bounding_rect.height()/2)
            if not room.subtype:
                scene.addRect(room.bounding_rect)
            elif room.subtype:
                scene.addEllipse(room.bounding_rect)
            # elif room.subtype == "Special":
            #     polygon = QPolygonF()
            #     tbw = max(50, room.bounding_rect.width())
            #     x_ = room.bounding_rect.x()
            #     y_ = room.bounding_rect.y()
            #     polygon.append(QPointF(x_ + tbw / 2, y_))
            #     polygon.append(QPointF(x_ + tbw, y_ + room.bounding_rect.height() / 2))
            #     polygon.append(QPointF(x_ + tbw / 2, y_ + room.bounding_rect.height()))
            #     polygon.append(QPointF(x_, y_ + room.bounding_rect.height() / 2))
            #     scene.addPolygon(polygon)

        pairs = {}
        for passage in listener.new_map.passages:
            from_room = passage.from_room
            to_room = passage.to_room
            if (to_room, from_room) in pairs:
                print("pair")
                current = pairs[(to_room, from_room)]
                pairs[(to_room, from_room)] = (current, passage)
            else:
                pairs[(from_room, to_room)] = passage
        
        for obj in pairs.values():
            if isinstance(obj, Passage):
                from_room = obj.from_room
                to_room = obj.to_room
                from_direction = obj.direction
                to_direction = opposite(obj.direction)
                from_point = attachment_point(from_room.subtype, from_room.bounding_rect, from_direction)
                to_point = attachment_point(to_room.subtype, to_room.bounding_rect, to_direction)
                line = scene.addLine(from_point.x(), from_point.y(), to_point.x(), to_point.y())
                if from_direction == 'u' or from_direction == 'd':
                    line.setPen(DASH_PEN)
                add_arrowhead(scene, to_point, from_point)
            else:
                from_room = obj[0].from_room
                to_room = obj[1].from_room
                from_direction = obj[0].direction
                to_direction = obj[1].direction
                from_point = attachment_point(from_room.subtype, from_room.bounding_rect, from_direction)
                to_point = attachment_point(to_room.subtype, to_room.bounding_rect, to_direction)
                line = scene.addLine(from_point.x(), from_point.y(), to_point.x(), to_point.y())
                if from_direction == 'u' or from_direction == 'd' or to_direction == 'u' or to_direction == 'd':
                    line.setPen(DASH_PEN)
                add_arrowhead(scene, to_point, from_point)
                add_arrowhead(scene, from_point, to_point)

                    


 
if __name__ == '__main__':
    mymap = Map()

    kalamontee ="""
[Courtyard]d<->[Winding Stair]
[Plain Hall]s<->[Courtyard]
[Plain Hall]n<->[Rec Area]
[Plain Hall]ne<->[Rec Corridor]
[Courtyard]w<->[West Wing]
[Rec Area]e<->[Rec Corridor]
[Rec Corridor]e<->[Mess Corridor]
[Mess Corridor]s<->[Mess Hall]
[Mess Hall]s<->[Kitchen]
[Mess Corridor]n<->[Storage West]
[Mess Corridor]e<->[Dorm Corridor]
[Rec Corridor]n<->[Dorm B]<
[Rec Corridor]s<->[Dorm A]<
[Dorm A]s<->[SanFac A]<
[Dorm B]n<->[SanFac B]<
[Dorm Corridor]n<->[Dorm D]<
[Dorm D]n<->[SanFac D]<
[Dorm Corridor]s<->[Dorm C]<
[Dorm C]s<->[SanFac C]<
[Dorm Corridor]e<->[Corridor Junction]
[Corridor Junction]n<->[Admin Corridor South]
[Admin Corridor South]e<->[SanFac E]
[Admin Corridor South]n<->[Admin Corridor]
[Corridor Junction]s<->[Mech Corridor North]
[Corridor Junction]e<->[Elevator Lobby]
[Elevator Lobby]e<->[Booth 2]
[Elevator Lobby]n<->[Upper Elevator]<
[Elevator Lobby]s<->[Lower Elevator]<
[Admin Corridor]n<->[Admin Corridor North]
[Admin Corridor]w<->[Systems Monitors]
[Mech Corridor North]e<->[Storage East]
[Mech Corridor North]w<->ne[Physical Plant]
[Mech Corridor North]s<->[Mech Corridor]
[Physical Plant]se<->w[Mech Corridor]
[Mech Corridor]e<->[Reactor Control]
[Mech Corridor]s<->[Mech Corridor South]
[Mech Corridor South]sw<->[Tool Room]
[Tool Room]e<->[Machine Shop]
[Mech Corridor South]s<->[Machine Shop]
[Mech Corridor South]se<->[Robot Shop]
[Machine Shop]e<->[Robot Shop]
[Reactor Control]e<->[Reactor Elevator]<
[Reactor Control]d-->?
[Admin Corridor North]w<->[Small Office]
[Admin Corridor North]n-->?
[Admin Corridor North]e<->[Plan Room]
[Small Office]w<->[Large Office]
[Booth 1]s<->[Conference Room]
[Conference Room]s<->[Rec Area]
"""
    tower="""
[Upper Elevator]s<->[Tower Core]
[Tower Core]ne<->[Comm Room]<
[Tower Core]u<->[Helipad]
[Tower Core]sw<->[Observation Deck]

"""
    kalamontee_shuttle_station="""
[Waiting Area]e<->[Kalamontee Platform]
[Waiting Area]s<->[Lower Elevator]
[Kalamontee Platform]s<->[Shuttle Car Alfie]
[Shuttle Car Alfie]e<->[Alfie Control East]<
[Shuttle Car Alfie]w<->[Alfie Control West]<
"""
    lawanda="""
[Alfie Control East]w<->[Shuttle Car Alfie]
[Shuttle Car Alfie]w<->[Alfie Control West]
[Shuttle Car Alfie]n<->[Lawanda Platform]
[Lawanda Platform]n<->[Shuttle Car Betty]
[Shuttle Car Betty]e<->[Betty Control East]
[Shuttle Car Betty]w<->[Betty Control West]
[Lawanda Platform]e<->[Escalator]
[Escalator]e<->[Fork]
[Fork]ne<->[Systems Corridor West]
[Fork]se<->[Project Corridor West]
[Project Corridor West]e<->[Project Corridor]
[Project Corridor]e<->[Project Corridor East]
[Project Corridor]s<->[ProjCon Office]
[ProjCon Office]e<->[Computer Room]
[Computer Room]n<->[Project Corridor East]
[Computer Room]ne<->[Main Lab]
[Computer Room]s<->[Miniaturization Booth]<
[Main Lab]ne<->w[Radiation Lock West]
[Radiation Lock West]e<->[Radiation Lock East]
[Radiation Lock East]e-->?
[Main Lab]se<->w[Bio Lock West]
[Bio Lock West]e<->[Bio Lock East]
[Bio Lock East]e<->[Bio Lab]
[Auxiliary Booth]n<->[Lab Office]
[Lab Office]w<->[Bio Lab]
[Main Lab]s<->[Lab Storage]<
[Project Corridor East]n<->[Library Lobby]
[Project Corridor East]e<->[Main Lab]
[Project Corridor West]w<->[SanFac F]
[Systems Corridor West]e<->[Systems Corridor]
[Systems Corridor]e<->[Systems Corridor East]
[Systems Corridor East]e<->[Physical Plant]
[Systems Corridor East]n<->[Course Control]
[Systems Corridor East]s<->[Library Lobby]
[Library Lobby]w<->[Library]
[Library Lobby]e<->[Booth 3]<
[Systems Corridor]n<->[Planetary Defense]
[Systems Corridor West]nw<->[Infirmary]
[Systems Corridor West]n<->[Repair Room]
[Repair Room]n-->*(Behind Small Door)
"""
    computer = """
[Station 384]e<->[Strip Near Station]
[Strip Near Station]n-->[Middle of Strip]
[Middle of Strip]n<->[Strip Near Relay]
"""

    input_stream = InputStream(lawanda)
    lexer = zmapLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = zmapParser(stream)
    tree = parser.parse()
    listener = zmapListenerImpl()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)
    listener.new_map.position_rooms()
    listener.new_map.graph().view()
    for room_name in listener.new_map.rooms:
        room = listener.new_map.rooms[room_name]
