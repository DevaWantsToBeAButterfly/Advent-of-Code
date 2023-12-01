from aocd import get_data, submit

puzzle_input = get_data(year=2018)
frequency = 0

for line in puzzle_input.splitlines():
    if line[0] == '+':
        frequency += int(line[1:])
    elif line[0] == '-':
        frequency -= int(line[1:])

print(frequency)
submit(frequency, part='a')

frequency = 0
past_frequencies = set()
running = True

while running:
    for line in puzzle_input.splitlines():
        if line[0] == '+':
            frequency += int(line[1:])
        elif line[0] == '-':
            frequency -= int(line[1:])
        if frequency in past_frequencies:
            print('yay')
            running = False
            break
        past_frequencies.add(frequency)

print(frequency)
submit(frequency, part='b')
