from generic_functions import read_lines
empty_spots = set()
sensors = []
beacons = []
puzzle_input = read_lines('./data_files/day_15_input.txt')

for line in puzzle_input:
    line = line.split(':')
    x_start = line[0].index('x') + 2
    x_end = line[0].index(',')
    y_start = line[0].index('y') + 2
    y_end = len(line[0])

    x = line[0][x_start:x_end]
    y = line[0][y_start:y_end]
    sensor_pos = (int(x), int(y))

    x_start = line[1].index('x') + 2
    x_end = line[1].index(',')
    y_start = line[1].index('y') + 2
    y_end = len(line[1])
    x = line[1][x_start:x_end]
    y = line[1][y_start:y_end]
    beacon_pos = (int(x), int(y))

    sensors.append(sensor_pos)
    beacons.append(beacon_pos)

wanted_row_empty_sections = []
empty_spots = set()
beacons_at_target_level = set()

for sensor, beacon in zip(sensors, beacons):
    taxi_distance = abs(sensor[0] - beacon[0]) + abs(sensor[1] - beacon[1])
    if 2000000 in range(sensor[1], sensor[1] + taxi_distance + 1) or 2000000 in range(sensor[1] - taxi_distance, sensor[1] + 1):
        y_offset = abs(sensor[1] - 2000000)
        empty_section = (sensor[0] - (taxi_distance - y_offset), sensor[0] + (taxi_distance - y_offset))
        wanted_row_empty_sections.append(empty_section)


for section in wanted_row_empty_sections:
    for n in range(section[0], section[1] + 1):
        empty_spots.add(n)

for beacon in beacons:
    if beacon[1] == 2000000:
        beacons_at_target_level.add(beacon)

print(len(empty_spots) - len(beacons_at_target_level))