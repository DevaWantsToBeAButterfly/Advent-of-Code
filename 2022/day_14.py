from generic_functions import read_lines
puzzle_input = read_lines('./data_files/day_14_input.txt')
walls = set()

for wall in puzzle_input:
    wall = wall.split(' -> ')
    wall_instructions = [(int(pos.split(',')[0]), int(pos.split(',')[1])) for pos in wall]
    starting_position = wall_instructions[0]
    walls.add(starting_position)
    for pos in wall_instructions[1:]:
        if starting_position[0] != pos[0]:
            for x_coord in range(min(starting_position[0], pos[0]), max(starting_position[0], pos[0]) + 1):
                walls.add((x_coord, starting_position[1]))

        elif starting_position[1] != pos[1]:
            for y_coord in range(min(starting_position[1], pos[1]), max(starting_position[1], pos[1]) + 1):
                walls.add((starting_position[0], y_coord))

        starting_position = pos


def spam_sand(cave_bottom, wall_spots):
    lowest_wall_spot = max([pos[1] for pos in wall_spots])
    solid_spots = wall_spots.copy()
    while True:
        sand_pos = [500, 0]
        while True:
            if sand_pos[1] > lowest_wall_spot:
                if cave_bottom == 'Endless Void':
                    print(len(solid_spots) - len(wall_spots))
                    return
                elif cave_bottom == 'Infinite Floor':
                    solid_spots.add(tuple(sand_pos))
                    break

            elif (sand_pos[0], sand_pos[1] + 1) not in solid_spots:
                sand_pos[1] += 1

            elif (sand_pos[0] - 1, sand_pos[1] + 1) not in solid_spots:
                sand_pos[0] -= 1
                sand_pos[1] += 1

            elif (sand_pos[0] + 1, sand_pos[1] + 1) not in solid_spots:
                sand_pos[0] += 1
                sand_pos[1] += 1

            else:
                solid_spots.add(tuple(sand_pos))
                if sand_pos == [500, 0]:
                    print(len(solid_spots) - len(wall_spots))
                    return
                break


spam_sand('Endless Void', walls)
spam_sand('Infinite Floor', walls)
