from generic_functions import read_lines

forest_map = [[int(tree) for tree in list(row)] for row in read_lines('.\data_files\day_8_input.txt')]
visible_trees = []

for y_index, row in enumerate(forest_map):
    for x_index, tree in enumerate(row):
        vertical_tree_line = [line[x_index] for line in forest_map]
        left_trees = set(row[:x_index])
        left_trees.add(-1)
        right_trees = set(row[x_index + 1:])
        right_trees.add(-1)
        up_trees = set(vertical_tree_line[:y_index])
        up_trees.add(-1)
        down_trees = set(vertical_tree_line[y_index + 1:])
        down_trees.add(-1)

        if tree > min(max(left_trees), max(right_trees), max(up_trees), max(down_trees)):
            visible_trees.append(tree)

print(len(visible_trees))
scenic_scores = []


def check_line_of_sight(tree_map, x_coord, y_coord, tree_height, direction, trees_seen):
    seen_trees = 0

    if direction == 'up':
        x_offset = 0
        y_offset = -1

    elif direction == 'down':
        x_offset = 0
        y_offset = 1

    elif direction == 'left':
        x_offset = -1
        y_offset = 0

    else:
        x_offset = 1
        y_offset = 0

    current_y_index = y_coord + y_offset
    current_x_index = x_coord + x_offset

    while (0 <= current_y_index <= len(tree_map) - 1) and (0 <= current_x_index <= len(tree_map[0]) - 1):
        seen_trees += 1

        if tree_map[current_y_index][current_x_index] >= tree_height:
            break

        current_y_index += y_offset
        current_x_index += x_offset

    trees_seen.append(seen_trees)
    return trees_seen


for y_index, row in enumerate(forest_map):
    for x_index, tree in enumerate(row):
        seen_trees_list = []
        for direction in ('up', 'down', 'left', 'right'):
            seen_trees_list = check_line_of_sight(forest_map, x_index, y_index, tree, direction, seen_trees_list)

        scenic_scores.append(seen_trees_list[0] * seen_trees_list[1] * seen_trees_list[2]*seen_trees_list[3])

print(max(scenic_scores))