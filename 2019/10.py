from math import gcd

with open('data_files\day_10_input') as input_file:
    space_data = [list(row.rstrip()) for row in input_file.readlines()]
    print(space_data)


def count_seen_asteroids(space_map):
    asteroids_list = []
    seen_counts = []

    for y in range(len(space_map)):
        row = space_map[y]
        for x in range(len(row)):
            if row[x] == '#':
                asteroids_list.append({'X': x, 'Y': y})

    for asteroid in asteroids_list:
        seen_counter = 0
        for other_asteroid in asteroids_list:
            blocked_view = False

            if asteroid == other_asteroid:
                continue

            asteroids_offset = [other_asteroid['X'] - asteroid['X'], other_asteroid['Y'] - asteroid['Y']]
            offset_divisor = gcd(asteroids_offset[0], asteroids_offset[1])
            steps_between_asteroids = [int(asteroids_offset[0] / offset_divisor), int(asteroids_offset[1] / offset_divisor)]

            current_pos = [asteroid['X'] + steps_between_asteroids[0], asteroid['Y'] + steps_between_asteroids[1]]

            while current_pos != [other_asteroid['X'], other_asteroid['Y']]:

                if space_map[current_pos[1]][current_pos[0]] == '#':
                    blocked_view = True
                    break

                current_pos[0] += steps_between_asteroids[0]
                current_pos[1] += steps_between_asteroids[1]

            if not blocked_view:
                seen_counter += 1

        seen_counts.append(seen_counter)

    print(max(seen_counts))


count_seen_asteroids(space_data)
