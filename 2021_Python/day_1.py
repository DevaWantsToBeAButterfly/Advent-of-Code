with open('data_files/day_1_input.txt') as input_file:
    depth_measurements = [int(n) for n in input_file.readlines()]

# ----PART 1----
increase_count = 0

for measure_1, measure_2 in zip(depth_measurements, depth_measurements[1:]):
    if measure_2 > measure_1:
        increase_count += 1

print(increase_count)

# ----PART 2----
group_increase_count = 0
previous_group_sum = float('inf')

for n in range(len(depth_measurements) - 2):
    current_group_sum = sum(depth_measurements[n:n + 3])
    if current_group_sum > previous_group_sum:
        group_increase_count += 1
    previous_group_sum = current_group_sum

print(group_increase_count)
