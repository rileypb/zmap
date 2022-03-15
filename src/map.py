import graphviz
import random

X_SCALE = 3
Y_SCALE = 3

opposites = { 'n': 's', 'ne': 'sw', 'e': 'w', 'se': 'nw', 's': 'n', 'sw': 'ne',
              'w': 'e', 'nw': 'se', 'u': 'd', 'd': 'u'}

def opposite(direction):
    return opposites[direction]


def get_x_change(direction):
    if 'e' in direction:
        return 1 + 0.05*random.random() - 0.025
    if 'w' in direction:
        return -1 + 0.05*random.random() - 0.025
    if 'd' in direction:
        return -1 + 0.05*random.random() - 0.025
    if 'u' in direction:
        return 1 + 0.05*random.random() - 0.025
    return 0


def get_y_change(direction):
    if 'n' in direction:
        return 1 + 0.05*random.random() - 0.025
    if 's' in direction:
        return -1 + 0.05*random.random() - 0.025
    if 'd' in direction:
        return -1 + 0.05*random.random() - 0.025
    if 'u' in direction:
        return 1 + 0.05*random.random() - 0.025
    return 0

scale_by_modifier = { '<': 0.5, '>': 2.0 }

def calculate_position_for(room):
    cx = 0
    cy = 0
    count = 0
    for passage in room.passages:
        opposite_room = passage.from_room if passage.to_room == room else passage.to_room
        if opposite_room and opposite_room.position:
            direction = passage.direction if passage.to_room == room else opposite(passage.direction)
            opposite_position = opposite_room.position
            scale = scale_by_modifier[passage.modifier] if passage.modifier else 1
            new_position = (opposite_position[0] + scale*get_x_change(direction), opposite_position[1] + scale*get_y_change(direction))
            cx += new_position[0]
            cy += new_position[1]
            count += 1
    room.position = (cx / count, cy / count)


class Passage:
    def __init__(self, from_room, direction, to_room=None, modifier=None) -> None:
        self.from_room = from_room
        self.direction = direction
        self.to_room = to_room
        self.from_room.passages.append(self)
        if to_room:
            to_room.passages.append(self)
        self.modifier = modifier

    def __str__(self):
        if self.to_room:
            return f'[{self.from_room}]{self.direction}-->[{self.to_room}]'
        else:
            return f'[{self.from_room}]{self.direction}-->?'


    def __repr__(self):
        return self.__str__()

class Room:
    def __init__(self, id, label, subtype=None) -> None:
        self.id = id
        if subtype == 'Unknown':
            label = '?'

        self.name = label
        self.label = label
        self.subtype = subtype
        self.position = None
        self.passages = []

    def __str__(self):
        return f'[{self.label}]'

    def __repr__(self):
        return self.__str__()

class Map:
    def __init__(self) -> None:
        self.first_room = None
        self.rooms = {}
        self.passages = []

    def add_room(self, id, label=None, subtype=None):
        if id not in self.rooms.keys():
            room = Room(id, label=label, subtype=subtype)
            self.rooms[id] = room
            if not self.first_room:
                self.first_room = room

    def add_passage(self, from_room, from_dir, to_room, modifier=None):
        from_passage = Passage(from_room, from_dir, to_room, modifier=modifier)
        self.passages.append(from_passage)

    def position_rooms(self):
        rooms_by_position = {}
        current_node = self.first_room
        current_node.position = (0, 0)
        frontier = [current_node]
        while frontier:
            current_node = frontier.pop(0)
            for passage in current_node.passages:
                next_room = passage.from_room if passage.to_room == current_node else passage.to_room
                if not next_room or next_room.position:
                    continue
                frontier.append(next_room)
                calculate_position_for(next_room)
                if next_room.position in rooms_by_position:
                    print("collision")
                rooms_by_position[next_room.position] = next_room


    def graph(self):
        pairs = {}
        for passage in self.passages:
            from_room = passage.from_room
            to_room = passage.to_room
            if (to_room, from_room) in pairs:
                print("pair")
                current = pairs[(to_room, from_room)]
                pairs[(to_room, from_room)] = (current, passage)
            else:
                pairs[(from_room, to_room)] = passage

        g = graphviz.Digraph('G', filename='zmap.gv', engine="fdp")
        g.attr(splines="TRUE")
        g.attr(K="0")
        rooms = list(self.rooms.values())
        random.shuffle(rooms)
        print(rooms)
        for room in rooms:
            shape = "rectangle" if not room.subtype else {"Unknown": "ellipse", "Special": "diamond"}[room.subtype]
            g.node(str(room.id), label=room.label, shape=shape, fontsize="11", pos=f'{X_SCALE*room.position[0]},{X_SCALE*room.position[1]}!', height="1", width="1")
        for key in pairs:
            obj = pairs[key]
            print(obj)
            if isinstance(obj, Passage):
                tailport = obj.direction
                if tailport == 'u':
                    tailport = 'n'
                if tailport == 'd':
                    tailport = 's'
                if obj.to_room is None:
                    to_room_name = f'{id(obj)}_?'
                    to_room_label = "?"
                    #g.node(to_room_name, label=to_room_label) #, pos=f'{X_SCALE/2*obj.from_room.position[0]},{Y_SCALE/2*obj.from_room.position[1]}')
                else:
                    to_room_name = str(obj.to_room.id)
                    to_room_label = str(obj.to_room.id)
                if obj.direction in ['e', 'w']:
                    constraint = "FALSE"
                else:
                    constraint = "FALSE"
                if obj.direction not in ['s', 'se', 'sw']:
                    g.edge(to_room_name, str(obj.from_room.id), headlabel=obj.direction, headport=tailport, tailport=opposite(tailport), dir="back", labelfloat="TRUE", labeldistance="1.5", constraint=constraint)
                else:
                    g.edge(str(obj.from_room.id), to_room_name, taillabel=obj.direction, tailport=tailport, headport=opposite(tailport), labelfloat="TRUE", labeldistance="1.5", constraint=constraint)
            else:
                p1 = obj[0]
                p2 = obj[1]
                tailport = p1.direction
                if tailport == 'u':
                    tailport = 'n'
                if tailport == 'd':
                    tailport = 's'
                headport = p2.direction
                if headport == 'u':
                    headport = 'n'
                if headport == 'd':
                    headport = 's'
                if p1.direction in ['e','w']:
                    constraint = "FALSE"
                    minlen="2"
                    weight="0"
                else:
                    constraint = "FALSE"
                    minlen = "2"
                    weight="0"
                if p1.direction in ['s', 'sw', 'w', 'nw', 'd']:
                    g.edge(p1.from_room.id, p1.to_room.id, taillabel=p1.direction, tailport=tailport, constraint=constraint,
                        dir="both", headlabel=p2.direction, headport=headport, labelfloat="TRUE", labeldistance="1.5",
                        minlen=minlen, weight=weight)
                else:
                    g.edge(p1.to_room.id, p1.from_room.id, taillabel=p2.direction, tailport=headport, constraint=constraint,
                        dir="both", headlabel=p1.direction, headport=tailport, labelfloat="TRUE", labeldistance="1.5",
                        minlen=minlen, weight=weight)
            
        

        return g

