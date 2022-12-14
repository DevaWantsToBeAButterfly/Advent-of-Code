from intcode_computer import IntcodeComputer
from itertools import permutations

with open('data_files\day_7_input.txt') as input_file:
    instructions_list = [int(n) for n in input_file.read().split(',')]

settings_sequences_list = list(permutations(range(5), 5))
thrusters_signals = []

intcode_computer = IntcodeComputer(instructions_list, False)

for sequence in settings_sequences_list:
    intcode_computer.update_input([sequence[0], 0])
    first_amplifier_output = intcode_computer.execute_program()

    intcode_computer.update_input([sequence[1], first_amplifier_output[-1]])
    second_amplifier_output = intcode_computer.execute_program()

    intcode_computer.update_input([sequence[2], second_amplifier_output[-1]])
    third_amplifier_output = intcode_computer.execute_program()

    intcode_computer.update_input([sequence[3], third_amplifier_output[-1]])
    fourth_amplifier_output = intcode_computer.execute_program()

    intcode_computer.update_input([sequence[4], fourth_amplifier_output[-1]])
    fifth_amplifier_output = intcode_computer.execute_program()

    thrusters_signals.append(fifth_amplifier_output)

print(max(thrusters_signals))