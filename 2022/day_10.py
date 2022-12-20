from generic_functions import read_lines

current_cycle = 0
current_x = 1
signal_strength_values = []
puzzle_input = read_lines('./data_files/day_10_input.txt')
pixels = []


def process_cycle(cycle_num, x_num, signal_strength_list, pixel_map):
    # There's an off-by-one error on rows 3-4 and 4-5, but I can't figure it out
    cycle_num += 1
    cycle_pos = (cycle_num - 1) % 40
    x_pos = x_num % 40 - x_num // 40
    if cycle_pos in (x_pos - 1, x_pos, x_pos + 1):
        pixel_map.append('O')
    else:
        pixel_map.append(' ')

    if cycle_num in (20, 60, 100, 140, 180, 220):
        signal_strength_list.append(cycle_num * x_num)

    return cycle_num, x_num, signal_strength_list, pixel_map


for line in puzzle_input:
    current_cycle, current_x, signal_strength_values, pixels =\
        process_cycle(line, current_cycle, current_x, signal_strength_values, pixels)

    if line.startswith('a'):
        current_cycle, current_x, signal_strength_values, pixels = \
            process_cycle(line, current_cycle, current_x, signal_strength_values, pixels)
        current_x += int(line.split(' ')[1])


print(sum(signal_strength_values))
print(pixels)
