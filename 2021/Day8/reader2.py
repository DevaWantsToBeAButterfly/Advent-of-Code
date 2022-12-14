with open("badOutput.txt") as input_file:
    input_text = input_file.read()

input_text = input_text.replace("\n", "")

with open("formattedInput.txt", "w") as formatted_input_file:
    formatted_input_file.write(input_text)
