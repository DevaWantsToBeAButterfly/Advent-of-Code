with open("data_files/day_3_input.txt") as input_file:
    wire_paths = input_file.readlines()
    wire_paths[0] = wire_paths[0].replace("\n", "").split(",")
    wire_paths[1] = wire_paths[1].replace("\n", "").split(",")

moves_dict = {
    "U": [0, 1],
    "D": [0, -1],
    "R": [1, 0],
    "L": [-1, 0],
}


def map_wire(wire_path):
    wire_pos = [0, 0]
    wire_movements = [{'Coordinates': [0, 0], 'Travel distance': 0}]
    travelled_distance = 0

    for step in wire_path:
        step_direction = step[0]
        step_distance = int(step[1:])
        x_start = wire_pos[0]
        x_end = x_start + (step_distance * moves_dict[step_direction][0])
        y_start = wire_pos[1]
        y_end = y_start + (step_distance * moves_dict[step_direction][1])

        wire_pos = [x_end, y_end]
        travelled_distance += get_distance_between(x_start, x_end) + get_distance_between(y_start, y_end)

        wire_movements.append({'Coordinates': wire_pos, 'Travel distance': travelled_distance})

    return wire_movements


def get_distance_between(point_a, point_b):

    return abs(max(point_a, point_b) - min(point_a, point_b))


def find_intersections(first_wire_spots, second_wire_spots):
    intersections = []

    for first_wire_spot, first_wire_next_spot in zip(first_wire_spots, first_wire_spots[1:]):
        x_start_1 = first_wire_spot['Coordinates'][0]
        y_start_1 = first_wire_spot['Coordinates'][1]

        x_end_1 = first_wire_next_spot['Coordinates'][0]
        y_end_1 = first_wire_next_spot['Coordinates'][1]

        for second_wire_spot, second_wire_next_spot in zip(second_wire_spots, second_wire_spots[1:]):
            x_start_2 = second_wire_spot['Coordinates'][0]
            y_start_2 = second_wire_spot['Coordinates'][1]

            x_end_2 = second_wire_next_spot['Coordinates'][0]
            y_end_2 = second_wire_next_spot['Coordinates'][1]

            first_wire_spot_distance = first_wire_spot['Travel distance']
            second_wire_spot_distance = second_wire_spot['Travel distance']

            if x_start_1 == x_end_1:
                if (x_start_2 <= x_start_1 <= x_end_2) and (y_start_1 <= y_start_2 <= y_end_1):
                    first_wire_total_distance = first_wire_spot_distance + get_distance_between(y_start_1, y_start_2)
                    second_wire_total_distance = second_wire_spot_distance + get_distance_between(x_start_1, x_start_2)
                    intersections.append({'Coordinates': [x_start_1, y_start_2],
                                          'First wire distance': first_wire_total_distance,
                                          'Second wire distance': second_wire_total_distance})
            else:
                if (x_start_1 <= x_start_2 <= x_end_1) and (y_start_2 <= y_start_1 <= y_end_2):
                    first_wire_total_distance = first_wire_spot_distance + get_distance_between(x_start_1, x_start_2)
                    second_wire_total_distance = second_wire_spot_distance + get_distance_between(y_start_1, y_start_2)
                    intersections.append({'Coordinates': [x_start_2, y_start_1],
                                          'First wire distance': first_wire_total_distance,
                                          'Second wire distance': second_wire_total_distance})

    intersections.remove(intersections[0])
    return intersections


def find_nearest_intersection(intersections):

    smallest_distance = 999999999

    for intersection in intersections:
        intersection_distance = abs(intersection['Coordinates'][0]) + abs(intersection['Coordinates'][1])
        if intersection_distance < smallest_distance:
            smallest_distance = intersection_distance

    return smallest_distance


def find_least_travel_intersection(intersections):
    shortest_travel = 999999999

    for intersection in intersections:
        intersection_total_travel = intersection['First wire distance'] + intersection['Second wire distance']
        if intersection_total_travel < shortest_travel:
            shortest_travel = intersection_total_travel

    return shortest_travel


def solve():
    first_wire_path = map_wire(wire_paths[0])
    second_wire_path = map_wire(wire_paths[1])
    intersections = find_intersections(first_wire_path, second_wire_path)

    print("Solution to part 1: " + str(find_nearest_intersection(intersections)))
    print("Solution to part 2: " + str(find_least_travel_intersection(intersections)))


solve()
