from intcode_computer import IntcodeComputer

with open('data_files\day_5_input.txt') as input_file:
    instructions_list = [int(n) for n in input_file.read().split(',')]


intcode_computer = IntcodeComputer(instructions_list, True, [1])

print(intcode_computer.execute_program())

intcode_computer.update_input([5])
print(intcode_computer.execute_program())
