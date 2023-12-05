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
                new_seed_value = line[0] + abs(new_seed_value - line[1])
                break
    seed_locations.append(new_seed_value)

print(min(seed_locations))
submit(min(seed_locations), part='a')

# seed_groups = []
# split_seed_groups = []
# n = 0
#
# while n < len(seeds_list):
#     seed_groups.append({'Starting seed': seeds_list[n], 'Range': seeds_list[n + 1]})
#     n += 2
#
# for seed_group in seed_groups:
#     start_seed = seed_group['Starting seed']
#     seed_range = seed_group['Range']
#
#     for swap_map in maps_data:
#         print('ooooh', seed_group)
#         for line in swap_map['data']:
#             map_destination = line[0]
#             map_start = line[1]
#             map_range = line[2]
#
#             # Either lower and never able to reach map, or higher and never reached by map
#             if start_seed + seed_range < map_start:
#                 break
#             if start_seed > map_start + map_range:
#
#             # Initial seed lower than map start but eventually reaches it given its range
#             if start_seed < map_start <= start_seed + seed_range:
#                 split_seed_groups.append({'Starting seed': map_start, 'Range': seed_range - (map_start - start_seed)})
#
#                 quit()
#             if line[1] <= start_seed < line[1] + line[2]:
#                 new_seed_value = line[0] + abs(new_seed_value - line[1])
#                 break
#     seed_locations.append(new_seed_value)