from aocd import get_data, submit

puzzle_input = get_data(year=2023, day=9).splitlines()
running_total = 0
second_running_total = 0


def find_next_num(line):
    new_line = [int(line[n + 1]) - int(line[n]) for n in range(len(line) - 1)]

    if set(new_line) == {0}:
        return int(line[-1])
    else:
        return int(line[-1]) + find_next_num(new_line)


def find_prev_num(line):
    new_line = [int(line[n + 1]) - int(line[n]) for n in range(len(line) - 1)]

    if set(new_line) == {0}:
        return int(line[0])
    else:
        return int(line[0]) - find_prev_num(new_line)


for line in puzzle_input:
    next_number = find_next_num(line.split())
    running_total += next_number

    prev_number = find_prev_num(line.split())
    second_running_total += prev_number

print(running_total)
submit(running_total, part='a')
print(second_running_total)
submit(second_running_total, part='b')
