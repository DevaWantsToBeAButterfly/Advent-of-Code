from aocd import get_data, submit

input_data = get_data(year=2023, day=5).splitlines()

seeds_list = [int(seed) for seed in input_data[0].replace('seeds: ', '').split()]
maps_data = [{'name': 'seed-to-soil', 'start': 0, 'end': 0, 'data': []},
             {'name': 'soil-to-fertilizer', 'start': 0, 'end': 0, 'data': []},
             {'name': 'fertilizer-to-water', 'start': 0, 'end': 0, 'data': []},
             {'name': 'water-to-light', 'start': 0, 'end': 0, 'data': []},
             {'name': 'light-to-temperature', 'start': 0, 'end': 0, 'data': []},
             {'name': 'temperature-to-humidity', 'start': 0, 'end': 0, 'data': []},
             {'name': 'humidity-to-location', 'start': 0, 'end': 0, 'data': []}]

map_to_build = 0
for line_index, line in enumerate(input_data):
    if maps_data[map_to_build]['name'] in line:
        maps_data[map_to_build]['start'] = line_index + 1

        if map_to_build - 1 >= 0:
            maps_data[map_to_build - 1]['end'] = line_index - 1

        map_to_build += 1
        if map_to_build >= len(maps_data):
            break

maps_data[-1]['end'] = len(input_data)

for num_map in maps_data:
    num_map['data'] = [[int(num) for num in line.split()] for line in input_data[num_map['start']:num_map['end']]]

seed_locations = []

for seed in seeds_list:
    new_seed_value = seed
    for swap_map in maps_data:
        for line in swap_map['data']:
            if line[1] <= new_seed_value < line[1] + line[2]:
                new_seed_value += line[0] - line[1]
                break
    seed_locations.append(new_seed_value)

print(min(seed_locations))
submit(min(seed_locations), part='a')

seed_groups = []
n = 0

while n < len(seeds_list):
    seed_groups.append({'Starting seed': seeds_list[n], 'Range': seeds_list[n + 1]})
    n += 2

n = 0

while True:
    starting_n = n
    current_n_value = n

    for swap_map in maps_data[::-1]:
        for line in swap_map['data']:
            destination = line[0]
            start = line[1]
            line_range = line[2]
            if destination <= current_n_value < destination + line_range:
                current_n_value = start + current_n_value - destination
                break

    for seed in seed_groups:
        if seed['Starting seed'] <= current_n_value < seed['Starting seed'] + seed['Range']:
            print(starting_n)
            submit(starting_n, part='b')
            quit()

    n += 1
