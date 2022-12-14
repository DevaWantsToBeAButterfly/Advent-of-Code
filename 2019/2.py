from intcode_computer import IntcodeComputer

with open('data_files\day_2_input.txt') as input_file:
    instructions_list = [int(n) for n in input_file.read().split(',')]
    instructions_list[1] = 12
    instructions_list[2] = 2


intcode_computer = IntcodeComputer(instructions_list, False)
intcode_computer.execute_program()
print(intcode_computer.instructions[0])

intcode_computer.search_inputs(19690720)