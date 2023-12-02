from aocd import get_data, submit

puzzle_input = get_data(day=13, year=2020).splitlines()
min_wait = [999999999, None]

current_time = int(puzzle_input[0])
bus_periods = [int(t) for t in puzzle_input[1].split(',') if t != 'x']

for period in bus_periods:
    if period - current_time % period < min_wait[0]:
        min_wait = [period - current_time % period, period]

print(min_wait[0] * min_wait[1])
#submit(min_offset[0]*min_offset[1], part='a', day=13, year=2020)