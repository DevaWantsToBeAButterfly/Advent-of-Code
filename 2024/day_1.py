from aocd import get_data, submit

puzzle_input = get_data(year=2024, day=1).splitlines()

left_list = [int(pair.split()[0]) for pair in puzzle_input]
left_list.sort()
right_list = [int(pair.split()[1]) for pair in puzzle_input]
right_list.sort()

total_distance = 0

for n in range(len(puzzle_input)):
    total_distance += abs(right_list[n] - left_list[n])

submit(total_distance, 'a')

sim_score = 0

for num in left_list:
    appearances = [n for n in right_list if n==num]
    sim_score += num*len(appearances)

submit(sim_score, 'b')

