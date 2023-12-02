import math
from aocd import get_data, submit

max_cubes = {'red': 12, 'green': 13, 'blue': 14}
possible_games = set()
input_data = get_data().splitlines()

for game in input_data:
    game = game.replace('Game ', '')
    game_id = int(game[:game.index(':')])
    game_sets_list = game[game.index(':') + 2:].split('; ')
    game_is_possible = True

    while game_is_possible:
        for game_set in game_sets_list:
            cubes_list = game_set.split(', ')
            for cube in cubes_list:
                cube_count, cube_colour = cube.split(' ')
                if max_cubes[cube_colour] < int(cube_count):
                    game_is_possible = False
                    break
        break

    if game_is_possible:
        possible_games.add(game_id)

print(sum(possible_games))
submit(sum(possible_games))

cube_sets_powers = []

for game in input_data:
    cube_list = game[game.index(':') + 2:].replace('; ', ', ').split(', ')
    least_needed_cubes = {'red': 0, 'green': 0, 'blue': 0}
    for cube in cube_list:
        cube_count, cube_colour = cube.split(' ')
        if least_needed_cubes[cube_colour] < int(cube_count):
            least_needed_cubes[cube_colour] = int(cube_count)

    cube_sets_powers.append(math.prod(least_needed_cubes.values()))

print(sum(cube_sets_powers))
submit(sum(cube_sets_powers))
