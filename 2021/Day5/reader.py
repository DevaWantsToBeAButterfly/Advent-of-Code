with open("rawinput.txt") as input_file:
    input_text = input_file.read()

formatted_input = input_text.replace("\n", "]],[[")
formatted_input = "[[" + formatted_input.replace("->", "],[") + "]]"

with open("formattedInput.txt", "w") as formatted_input_file:
    formatted_input_file.write(formatted_input)
