from intcode_computer import IntcodeComputer

with open('data_files\\base_input.txt') as input_file:
    instructions_list = [int(n) for n in input_file.read().split(',')]


intcode_computer = IntcodeComputer(instructions_list)
intcode_computer.execute_program()