from map import *
import math

SPRING_LENGTH = 0.5
SPRING_FACTOR = 5
NODE_REPULSION_FACTOR = 0.1
TIME_STEP = 0.01


opposites = { 'n': 's', 'ne': 'sw', 'e': 'w', 'se': 'nw', 's': 'n', 'sw': 'ne',
              'w': 'e', 'nw': 'se', 'u': 'd', 'd': 'u'}

def opposite(direction):
    return opposites[direction]    

def force_on(node, node2):
    vec1 = (node.position[0] - node2.position[0], node.position[1] - node2.position[1])
    distance = math.sqrt(vec1[0]**2 + vec1[1]**2)
    
    force_scale = NODE_REPULSION_FACTOR/((distance + 0.001)**2)
    force = (vec1[0] * force_scale, vec1[1] * force_scale)
    return force

class Layout:
    def one_step(self, map):
        force_by_node = {}
        node: Room
        for node in map.rooms.values():
            if (node.free()):
                node2: Room
                total_force = (0, 0)
                for node2 in map.rooms.values():
                    if node2 == node:
                        continue
                    force = force_on(node, node2)
                    total_force = (total_force[0] + force[0], total_force[1] + force[1])

                for passage in node.passages:
                    opposite_room = passage.from_room if passage.to_room == node else passage.to_room
                    direction = passage.direction if passage.to_room == node else opposite(passage.direction)
                    opposite_position = opposite_room.position
                    scale = scale_by_modifier[passage.modifier] if passage.modifier else 1
                    if passage.to_room.subtype == 'Unknown':
                        scale = 0.5
                    ideal_position = (opposite_position[0] + scale*get_x_change(direction), opposite_position[1] + scale*get_y_change(direction))
                    
                    vec = (ideal_position[0] - node.position[0], ideal_position[1] - node.position[1])
                    dd = math.sqrt(vec[0]**2 + vec[1]**2)
                    force = (vec[0] * SPRING_FACTOR * dd, vec[1] * SPRING_FACTOR * dd)
                    total_force = (total_force[0] + force[0], total_force[1] + force[1])

                force_by_node[node] = total_force


            else:
                force_by_node[node] = (0, 0)
        
        for node in map.rooms.values():
            pos = node.position
            force = force_by_node[node]
            pos = (pos[0] + force[0] * TIME_STEP, pos[1] + force[1] * TIME_STEP)
            node.position = pos