with open('data_files/day_24_input.txt') as input_file:
    commands = input_file.read().splitlines()

values = {'w': 0, 'x': 0, 'y': 0, 'z': 0}
variables = ['w', 'x', 'y', 'z']
current_input_index = 0
model_number = '13579246899999'

for command in commands:
    operation = command[:3]
    first_variable_key = command[4]
    first_variable_value = values.get(first_variable_key)
    if operation == 'inp':
        values[first_variable_key] = int(model_number[current_input_index])
    else:
        second_variable_key = command[6]
        second_variable_value = values.get(second_variable_key)
        if second_variable_value is None:
            if second_variable_key == '-':
                second_variable_key = command[7]
                second_variable_value = int(second_variable_key) * -1
            else:
                second_variable_value = int(second_variable_key)
        match operation:
            case 'add':
                values[first_variable_key] = first_variable_value + second_variable_value
            case 'mul':
                values[first_variable_key] = first_variable_value * second_variable_value
            case 'div':
                values[first_variable_key] = first_variable_value // second_variable_value
            case 'mod':
                values[first_variable_key] = first_variable_value % second_variable_value
            case 'eql':
                if first_variable_value == second_variable_value:
                    values[first_variable_key] = 1
                else:
                    values[first_variable_key] = 0

print(values)
