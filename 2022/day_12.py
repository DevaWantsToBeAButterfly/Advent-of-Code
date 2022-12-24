from string import ascii_lowercase
from math import inf as infinite
from generic_functions import read_input


class Node:
    def __init__(self, x_coord, y_coord, height, is_start, is_end):
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.height = height
        self.is_start = is_start
        self.is_end = is_end
        self.distance_from_start = infinite
        self.neighbours = [None, None, None, None]  # UP, DOWN, LEFT, RIGHT

    def check_neighbours(self):
        neighbours_to_check = set()
        for neighbour in self.neighbours:
            if neighbour and neighbour.height - self.height <= 1:
                if neighbour.distance_from_start > self.distance_from_start + 1:
                    neighbour.distance_from_start = self.distance_from_start + 1
                    neighbours_to_check.add(neighbour)

        return neighbours_to_check

    def reset_distance(self):
        self.distance_from_start = infinite


def create_map_of_nodes(nodes_map_data):
    map_of_nodes = []
    for row_index, row in enumerate(nodes_map_data):
        map_of_nodes.append([])
        for col_index, spot in enumerate(row):
            spot_is_start, spot_is_end = False, False
            if spot == 'S':
                spot_height = 0
                spot_is_start = True
                start_node_pos = (row_index, col_index)
            elif spot == 'E':
                spot_height = ascii_lowercase.index('z')
                spot_is_end = True
                end_node_pos = (row_index, col_index)
            else:
                spot_height = ascii_lowercase.index(spot)

            map_of_nodes[row_index].append(Node(col_index, row_index, spot_height, spot_is_start, spot_is_end))

    find_nodes_neighbours(map_of_nodes)
    starting_node = map_of_nodes[start_node_pos[0]][start_node_pos[1]]
    ending_node = map_of_nodes[end_node_pos[0]][end_node_pos[1]]

    return map_of_nodes, starting_node, ending_node


def find_nodes_neighbours(map_of_nodes):
    for row in map_of_nodes:
        for node in row:
            if node.y_coord != 0:
                node.neighbours[0] = map_of_nodes[node.y_coord - 1][node.x_coord]

            if node.y_coord < len(map_of_nodes) - 1:
                node.neighbours[1] = map_of_nodes[node.y_coord + 1][node.x_coord]

            if node.x_coord != 0:
                node.neighbours[2] = map_of_nodes[node.y_coord][node.x_coord - 1]

            if node.x_coord < len(row) - 1:
                node.neighbours[3] = map_of_nodes[node.y_coord][node.x_coord + 1]


def find_shortest_path(starting_node, ending_node):
    starting_node.distance_from_start = 0
    nodes_to_check = set()
    nodes_to_check.add(starting_node)

    while nodes_to_check:
        new_nodes_to_check = set()
        for current_node in nodes_to_check:
            new_nodes_to_check.update(current_node.check_neighbours())

        nodes_to_check = new_nodes_to_check

    return ending_node.distance_from_start


def reset_nodes(map_of_nodes):
    for row in map_of_nodes:
        for node in row:
            node.is_start = False
            node.reset_distance()

    return map_of_nodes


def find_possible_scenic_starts(map_of_nodes):
    possible_starting_nodes = []

    for row in map_of_nodes:
        for node in row:
            if node.height == 0:
                possible_starting_nodes.append(node)

    return possible_starting_nodes


def calculate_all_scenic_paths(map_of_nodes, ending_node):
    scenic_paths_distances = set()
    scenic_starting_nodes = find_possible_scenic_starts(map_of_nodes)

    for starter_node in scenic_starting_nodes:
        map_of_nodes = reset_nodes(map_of_nodes)
        starter_node.is_start = True
        scenic_paths_distances.add(find_shortest_path(starter_node, ending_node))

    return scenic_paths_distances


puzzle_input = read_input('.\data_files\day_12_input.txt')
puzzle_input = [[spot for spot in list(row)] for row in puzzle_input.split('\n')]

nodes_map, start_node, end_node = create_map_of_nodes(puzzle_input)

print(find_shortest_path(start_node, end_node))
print(min(calculate_all_scenic_paths(nodes_map, end_node)))
