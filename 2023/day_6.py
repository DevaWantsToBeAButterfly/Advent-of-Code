import math
from aocd import submit

race_list = [{'Time': 42, 'Distance': 284, 'Ways to beat': 0}, {'Time': 68, 'Distance': 1005, 'Ways to beat': 0},
             {'Time': 69, 'Distance': 1122, 'Ways to beat': 0}, {'Time': 85, 'Distance': 1341, 'Ways to beat': 0}]

for race in race_list:
    seconds_held = 0

    while seconds_held < race['Time']:
        if seconds_held * (race['Time'] - seconds_held) >= race['Distance']:
            race['Ways to beat'] += 1
        seconds_held += 1

print(math.prod(race['Ways to beat'] for race in race_list))
submit(math.prod(race['Ways to beat'] for race in race_list), part='a')

real_race = {'Time': 42686985, 'Distance': 284100511221341, 'Ways to beat': 0}
seconds_held = 0

while seconds_held < real_race['Time']:
    if seconds_held * (real_race['Time'] - seconds_held) >= real_race['Distance']:
        real_race['Ways to beat'] += 1
    seconds_held += 1

print(real_race['Ways to beat'])
submit(real_race['Ways to beat'], part='b')
