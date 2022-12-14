with open('data_files/day_12.txt') as input_file:
    movements_list = [(line[0], int(line[1:])) for line in input_file.read().splitlines()]

north_value = 0
south_value = 0
east_value = 0
west_value = 0
faced_direction_degrees = 90

for movement in movements_list:
    match movement[0]:
        case 'N':
            north_value += movement[1]
        case 'S':
            south_value += movement[1]
        case 'E':
            east_value += movement[1]
        case 'W':
            west_value += movement[1]
        case 'L':
            faced_direction_degrees -= movement[1]
        case 'R':
            faced_direction_degrees += movement[1]
        case 'F':
            match faced_direction_degrees % 360:
                case 0:
                    north_value += movement[1]
                case 90:
                    east_value += movement[1]
                case 180:
                    south_value += movement[1]
                case 270:
                    west_value += movement[1]

print(abs(north_value - south_value) + abs(east_value - west_value))