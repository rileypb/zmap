from antlr4 import *  

from map import *

from PyQt5.QtCore import QRectF
from PyQt5.QtGui import QColor, QFont, QTextOption, QPolygonF, QBrush, QPen
from PyQt5.QtCore import Qt, QPointF
import math
from PyQt5.QtWidgets import (
    QGraphicsScene
)

import time


SPRING_LENGTH = 1
SPRING_FACTOR = 1
NODE_REPULSION_FACTOR = 1
NODE_ATTRACTION_FACTOR = 1
NODE_REPULSION_THRESHOLD = 4
TIME_STEP = 0.01

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


class GraphDisplay:
    def __init__(self, scene:QGraphicsScene) -> None:
        self.nodes = []
        self.edges = []
        self.scene = scene
        
    def add_node(self, room):
        pass

    def add_edge(self, passage):
        pass


class NodeDisplay:
    def __init__(self, room:Room) -> None:
        self.room = room

    def free(self) -> (bool):
        return self.room.free

    def pos(self):
        return self.room.position

    def force_on(self, node):
        vec1 = (node.pos()[0] - self.pos()[0], node.pos()[1] - self.pos()[1])
        distance = math.sqrt(vec1[0]**2 + vec1[1]**2)
        force_scale = -math.log(distance + 0.0001, NODE_REPULSION_THRESHOLD)
        if force_scale > 0: 
            force_scale *= NODE_REPULSION_FACTOR
        else:
            force_scale *= NODE_ATTRACTION_FACTOR
        force = (vec1[0] * force_scale, vec1[1] * force_scale)
        return force

    def move(self, force, time_step=1):
        new_pos = (self.pos()[0] + force[0]*time_step, self.pos()[1] + force[1]*time_step)
        self.room.position = new_pos



class EdgeDisplay:
    pass


class Layout:
    def __init__(self) -> None:
        self.complete = False

    def layout_one_step(self, graph:GraphDisplay) -> None:
        force_by_node = {}
        node: NodeDisplay
        for node in graph.nodes:
            if (node.free()):
                node2: NodeDisplay
                total_force = (0, 0)
                for node2 in graph.nodes:
                    if node2 == node:
                        continue
                    force = node2.force_on(node)
                    total_force[0] += force[0]
                    total_force[1] += force[1]
                force_by_node[node] = total_force
            else:
                force_by_node[node] = (0, 0)
        
        for node in graph.nodes:
            node.move(force_by_node[node], time_step=TIME_STEP)



    def display(self, map, scene):
        map.position_rooms()

        disp = GraphDisplay(scene)
        for room in map.rooms:
            disp.add_node(room)

        layout = Layout()

        for i in range(5):
            
            room_to_rect = {}

            for room in map.rooms.values():
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
                    room_to_rect[room] = scene.addRect(room.bounding_rect)
                elif room.subtype:
                    room_to_rect[room] = scene.addEllipse(room.bounding_rect)

            pairs = {}
            for passage in map.passages:
                from_room = passage.from_room
                to_room = passage.to_room
                if (to_room, from_room) in pairs:
                    current = pairs[(to_room, from_room)]
                    current.append(passage)
                elif (from_room, to_room) in pairs:
                    current = pairs[(from_room, to_room)]
                    current.append(passage)
                else:
                    pairs[(from_room, to_room)] = [passage]
            
            for passage in map.passages:
                if passage.two_way:
                    from_room = passage.from_room
                    to_room = passage.to_room
                    from_direction = passage.direction
                    to_direction = passage.back_direction
                    from_point = attachment_point(from_room.subtype, from_room.bounding_rect, from_direction)
                    to_point = attachment_point(to_room.subtype, to_room.bounding_rect, to_direction)
                    line = scene.addLine(from_point.x(), from_point.y(), to_point.x(), to_point.y())
                    if from_direction == 'u' or from_direction == 'd' or to_direction == 'u' or to_direction == 'd':
                        line.setPen(DASH_PEN)
                    add_arrowhead(scene, to_point, from_point)
                    add_arrowhead(scene, from_point, to_point)
                else:
                    from_room = passage.from_room
                    to_room = passage.to_room
                    from_direction = passage.direction
                    to_direction = opposite(passage.direction)
                    from_point = attachment_point(from_room.subtype, from_room.bounding_rect, from_direction)
                    to_point = attachment_point(to_room.subtype, to_room.bounding_rect, to_direction)
                    line = scene.addLine(from_point.x(), from_point.y(), to_point.x(), to_point.y())
                    if from_direction == 'u' or from_direction == 'd':
                        line.setPen(DASH_PEN)
                    add_arrowhead(scene, to_point, from_point)


                layout.layout_one_step(disp)

                time.sleep(0.01)