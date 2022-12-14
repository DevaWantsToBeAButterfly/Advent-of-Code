with open('data_files/day_11.txt') as input_file:
    starting_map = [['Floor' if spot == '.' else 'Empty' for spot in row] for row in input_file.read().splitlines()]

OFFSETS = [[-1, -1], [0, -1], [1, -1], [-1, 0], [1, 0], [-1, 1], [0, 1], [1, 1]]


def check_neighbour(seats, row, row_i, seat_i, x_offset, y_offset, mode):
    if mode == 'Part 1':
        if (0 <= seat_i + x_offset < len(row)) and (0 <= row_i + y_offset < len(seats)):
            return seats[row_i + y_offset][seat_i + x_offset]

    elif mode == 'Part 2':
        og_x_offset = x_offset
        og_y_offset = y_offset
        while (0 <= seat_i + x_offset < len(row)) and (0 <= row_i + y_offset < len(seats)):
            if seats[row_i + y_offset][seat_i + x_offset] != 'Floor':
                return seats[row_i + y_offset][seat_i + x_offset]
            else:
                x_offset += og_x_offset
                y_offset += og_y_offset


def get_surroundings(seats, row, row_i, seat_i, mode):
    surroundings = []
    for offset in OFFSETS:
        surroundings.append(check_neighbour(seats, row, row_i, seat_i, offset[0], offset[1], mode))

    return surroundings


def solve_part_1():
    seats_map = starting_map
    mode = 'Part 1'
    while True:
        updated_map = []
        for row_index, row in enumerate(seats_map):
            updated_map.append([])
            for seat_index, seat in enumerate(row):
                surrounding_seats = get_surroundings(seats_map, row, row_index, seat_index, mode)

                match seat:
                    case 'Floor':
                        updated_map[row_index].append('Floor')
                    case 'Empty':
                        if not surrounding_seats.count('Occupied'):
                            updated_map[row_index].append('Occupied')
                        else:
                            updated_map[row_index].append('Empty')
                    case 'Occupied':
                        if surrounding_seats.count('Occupied') >= 4:
                            updated_map[row_index].append('Empty')
                        else:
                            updated_map[row_index].append('Occupied')

        if seats_map == updated_map:
            break
        seats_map = updated_map

    print(sum([len([True for spot in row if spot == 'Occupied']) for row in seats_map]))


def solve_part_2():
    seats_map = starting_map
    mode = 'Part 2'
    while True:
        updated_map = []
        for row_index, row in enumerate(seats_map):
            updated_map.append([])
            for seat_index, seat in enumerate(row):
                surrounding_seats = get_surroundings(seats_map, row, row_index, seat_index, mode)

                match seat:
                    case 'Floor':
                        updated_map[row_index].append('Floor')
                    case 'Empty':
                        if not surrounding_seats.count('Occupied'):
                            updated_map[row_index].append('Occupied')
                        else:
                            updated_map[row_index].append('Empty')
                    case 'Occupied':
                        if surrounding_seats.count('Occupied') >= 5:
                            updated_map[row_index].append('Empty')
                        else:
                            updated_map[row_index].append('Occupied')

        if seats_map == updated_map:
            break
        seats_map = updated_map

    print(sum([len([True for spot in row if spot == 'Occupied']) for row in seats_map]))


solve_part_1()
solve_part_2()
