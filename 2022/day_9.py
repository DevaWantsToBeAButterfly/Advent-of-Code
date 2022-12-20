from generic_functions import read_lines


class Head:
    def __init__(self):
        self.x, self.y = 0, 0
        self.travel_offsets = {'L': (-1, 0), 'R': (1, 0), 'U': (0, -1), 'D': (0, 1)}
        self.child = None

    def travel_grid(self, instruction):
        travel_direction = instruction.split(' ')[0]
        travel_distance = int(instruction.split(' ')[1])

        for step in range(travel_distance):
            self.x += self.travel_offsets[travel_direction][0]
            self.y += self.travel_offsets[travel_direction][1]

            self.child.check_distance()


class TailNode:
    def __init__(self, parent):
        self.x, self.y = 0, 0
        self.parent = parent
        self.child = None
        self.visited_spots = [(0, 0)]

    def check_distance(self):
        parent_x = self.parent.x
        parent_y = self.parent.y
        if abs(self.x - parent_x) > 1:
            if parent_x > self.x:
                self.x += 1

            else:
                self.x -= 1

            if self.y != parent_y:
                if parent_y > self.y:
                    self.y += 1

                else:
                    self.y -= 1

        elif abs(self.y - parent_y) > 1:
            if parent_y > self.y:
                self.y += 1

            else:
                self.y -= 1

            if self.x != parent_x:
                if parent_x > self.x:
                    self.x += 1

                else:
                    self.x -= 1

        self.visited_spots.append((self.x, self.y))
        if self.child:
            self.child.check_distance()


def spawn_nodes(parent, current_node_number, total_nodes, nodes_list):
    next_node_number = current_node_number + 1
    current_node = TailNode(parent)
    nodes_list.append(current_node)

    if next_node_number <= total_nodes:
        nodes_list, child = spawn_nodes(current_node, next_node_number, total_nodes, nodes_list)
        current_node.child = child

    return nodes_list, current_node


rope_head = Head()
rope_nodes, rope_head.child = spawn_nodes(rope_head, 1, 1, [rope_head])
puzzle_input = read_lines('.\data_files\day_9_input.txt')

for line in puzzle_input:
    rope_head.travel_grid(line)

print(len(set(rope_head.child.visited_spots)))

rope_head = Head()
rope_nodes, rope_head.child = spawn_nodes(rope_head, 1, 9, [rope_head])

for line in puzzle_input:
    rope_head.travel_grid(line)

rope_tail = rope_nodes[-1]
print(len(set(rope_tail.visited_spots)))
# Saving this line as a comment for posterity
# print(len(set(rope_head.child.child.child.child.child.child.child.child.child.visited_spots)))
