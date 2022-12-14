with open('data_files/day_8.txt') as input_file:
    boot_code = [{'instruction': command.split(' ')[0], 'value': int(command.split(' ')[1]), 'was_run': False} for
                 command in input_file.read().splitlines()]
    print(boot_code)


def solve(boot_code_instructions):
    command_index = 0
    accumulator_number = 0
    while command_index < len(boot_code_instructions):
        command_instruction = boot_code_instructions[command_index].get('instruction')
        command_value = boot_code_instructions[command_index].get('value')

        if boot_code_instructions[command_index].get('was_run'):
            return accumulator_number, False
        elif command_instruction == 'acc':
            accumulator_number += command_value
        elif command_instruction == 'jmp':
            command_index += command_value - 1

        boot_code_instructions[command_index]['was_run'] = True
        command_index += 1

    return accumulator_number, True


def solve_2():
    fixed_infinite_loop = False
    command_to_change_index = 0
    while not fixed_infinite_loop:
        print(command_to_change_index)
        patched_boot_code = boot_code.copy()
        for command in patched_boot_code:
            command['was_run'] = False
        if patched_boot_code[command_to_change_index]['instruction'] == 'jmp':
            patched_boot_code[command_to_change_index]['instruction'] = 'nop'
        elif patched_boot_code[command_to_change_index]['instruction'] == 'nop':
            patched_boot_code[command_to_change_index]['instruction'] = 'jmp'
        else:
            command_to_change_index += 1
            continue
        print(patched_boot_code)
        accumulator_code, fixed_infinite_loop = solve(patched_boot_code.copy())
        print(accumulator_code, fixed_infinite_loop)
        command_to_change_index += 1

    print(accumulator_code)


print(solve(boot_code.copy()))
solve_2()
