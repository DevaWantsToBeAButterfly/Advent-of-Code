active_cubes = set()
with open('data_files/day_22_input.txt') as input_file:
    instructions_list = input_file.read().splitlines()


def execute_instruction(instruction):
    action = instruction[:3]
    instruction_start = instruction.index(' ')
    instruction_string = instruction[instruction_start:].replace('x=', '').replace('y=', '').replace('z=', '')
    instruction_pairs = instruction_string.split(',')
    instructions_list = [pair.split('..') for pair in instruction_pairs]
    x_start, x_end = int(instructions_list[0][0]), int(instructions_list[0][1]) + 1
    y_start, y_end = int(instructions_list[1][0]), int(instructions_list[1][1]) + 1
    z_start, z_end = int(instructions_list[2][0]), int(instructions_list[2][1]) + 1

    for x in range(x_start, x_end):
        for y in range(y_start, y_end):
            for z in range(z_start, z_end):
                if action == 'on ':
                    active_cubes.add((x, y, z))
                elif action == 'off':
                    if (x, y, z) in active_cubes:
                        active_cubes.remove((x, y, z))


for inst in instructions_list:
    print('doing line', instructions_list.index(inst))
    execute_instruction(inst)

print(len(active_cubes))
