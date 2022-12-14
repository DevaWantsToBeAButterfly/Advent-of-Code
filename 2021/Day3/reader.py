with open('rawInput.txt') as input_file:
    input_var = input_file.read()

formatted_input = "'" + input_var.replace('\n', "','") + "'"

with open('formattedInput.txt', 'w') as formatted_input_file:
    formatted_input_file.write(formatted_input)
