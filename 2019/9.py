from intcode_computer import IntcodeComputer

with open('data_files\\day_9_input.txt') as input_file:
    instructions_list = [int(n) for n in input_file.read().split(',')]


intcode_computer = IntcodeComputer(instructions_list, True, [2])
intcode_computer.execute_program()