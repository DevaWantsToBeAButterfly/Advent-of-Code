with open('data_files/day_2_input.txt') as input_file:
    raw_data = input_file.read()
    commands_list = raw_data.splitlines()

# ----PART 1----
horizontal_position = 0
depth = 0

for command in commands_list:
    command_identifier = command[0]
    command_distance = int(command[-1])

    match command_identifier:
        case 'f':
            horizontal_position += command_distance
        case 'u':
            depth -= command_distance
        case 'd':
            depth += command_distance

print(horizontal_position * depth)

# ---- PART 2----
horizontal_position = 0
depth = 0
aim = 0

for command in commands_list:
    command_identifier = command[0]
    command_distance = int(command[-1])

    match command_identifier:
        case 'f':
            horizontal_position += command_distance
            depth += (aim * command_distance)
        case 'u':
            aim -= command_distance
        case 'd':
            aim += command_distance

print(horizontal_position * depth)
