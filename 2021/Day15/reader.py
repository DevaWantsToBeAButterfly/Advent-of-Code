with open("rawInput.txt") as input_file:
    input_text = input_file.readlines()

output_text = ""

for line in input_text:
    for char in line:
        output_text += (
            "{ distance:" + char + ", shortestPath: Infinity, visited: false },"
        )
    output_text += "],["

output_text.replace(",{ distance:, shortestPath: Infinity },", "")


with open("formattedInput.txt", "w") as formatted_input_file:
    formatted_input_file.write(output_text)
