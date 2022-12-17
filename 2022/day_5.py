import copy

from generic_functions import read_input

puzzle_input = read_input('.\data_files\day_5_input.txt')
initial_state_data = [line.replace('\n', '') for line in puzzle_input[:8]]
moves_list = [line.replace('\n', '').split(' ') for line in puzzle_input[10:]]
starting_crane_map = [[] for n in range(9)]

for crane_row in initial_state_data:
    # lowest index in the list means highest crane in the column
    i = 1
    while i < len(crane_row):
        if crane_row[i] != ' ':
            starting_crane_map[i//4].append(crane_row[i])
        i += 4

crane_map = copy.deepcopy(starting_crane_map)

for instruction in moves_list:
    cranes_moved_count = int(instruction[1])
    source_column = crane_map[int(instruction[3]) - 1]
    target_column = crane_map[int(instruction[5]) - 1]

    for n in range(cranes_moved_count):
        moved_crane = source_column[0]
        target_column.insert(0, moved_crane)
        source_column.pop(0)

print([col[0] for col in crane_map])
crane_map = copy.deepcopy(starting_crane_map)

for instruction in moves_list:
    cranes_moved_count = int(instruction[1])
    source_column = crane_map[int(instruction[3]) - 1]
    target_column = crane_map[int(instruction[5]) - 1]
    moved_cranes = source_column[0:cranes_moved_count]

    for n in range(cranes_moved_count):
        source_column.pop(0)
        target_column.insert(0, moved_cranes[-1])
        moved_cranes.pop(-1)

print([col[0] for col in crane_map])