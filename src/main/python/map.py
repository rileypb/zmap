"""
Map, Passage and Room models.
"""

import random

opposites = { 'n': 's', 'ne': 'sw', 'e': 'w', 'se': 'nw', 's': 'n', 'sw': 'ne',
              'w': 'e', 'nw': 'se', 'u': 'd', 'd': 'u'}

def opposite(direction):
    return opposites[direction]


def get_x_change(direction):
    if 'e' in direction:
        return 1
    if 'w' in direction:
        return -1
    if 'd' in direction:
        return -1
    if 'u' in direction:
        return 1
    return 0


def get_y_change(direction):
    if 'n' in direction:
        return 1
    if 's' in direction:
        return -1
    if 'd' in direction:
        return -1
    if 'u' in direction:
        return 1
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
            if passage.to_room.subtype == 'Unknown':
                scale = 0.5
            new_position = (opposite_position[0] + scale*get_x_change(direction), opposite_position[1] + scale*get_y_change(direction))
            cx += new_position[0]
            cy += new_position[1]
            count += 1

            if not passage.to_room.subtype:
                opposite_direction = passage.back_direction if passage.from_room == room else opposite(passage.back_direction)
                new_position = (opposite_position[0] + scale * get_x_change(opposite_direction), opposite_position[1] + scale * get_y_change(opposite_direction))
                cx += new_position[0]
                cy += new_position[1]
                count += 1

    room.position = (cx / max(1, count), cy / max(1, count))


class Passage:
    def __init__(self, from_room, direction, to_room=None, back_direction=None, modifier=None, two_way=False) -> None:
        self.from_room = from_room
        self.direction = direction
        self.to_room = to_room
        self.from_room.passages.append(self)
        if to_room:
            to_room.passages.append(self)
        self.modifier = modifier
        self.two_way = two_way
        if back_direction:
            self.back_direction = back_direction
        else:
            self.back_direction = opposite(direction)

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

    def add_passage(self, from_room, from_dir, to_room=None, back_direction=None, modifier=None, two_way=False):
        from_passage = Passage(from_room, from_dir, to_room=to_room, back_direction=back_direction, modifier=modifier, two_way=two_way)
        self.passages.append(from_passage)

    def position_rooms(self):
        if not self.first_room:
            return
        rooms_by_position = {}
        all_rooms = list(self.rooms.values())
        current_node = self.first_room
        current_node.position = (0, 0)
        frontier = [current_node]
        while all_rooms or frontier:
            while frontier:
                current_node = frontier.pop(0)
                all_rooms.remove(current_node)
                for passage in current_node.passages:
                    next_room = passage.from_room if passage.to_room == current_node else passage.to_room
                    if not next_room or next_room.position:
                        continue
                    frontier.append(next_room)
                    calculate_position_for(next_room)
                    rooms_by_position[next_room.position] = next_room
            if all_rooms:
                one_room = random.choice(all_rooms)
                frontier.append(one_room)
                one_room.position = (0, 0)


    
