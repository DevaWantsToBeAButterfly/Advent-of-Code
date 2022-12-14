unique_inputs = []
output_values = []
fullOutput = []
with open("rawInput.txt") as input_file:
    input_text = input_file.readlines()

for line in input_text:
    line = line.replace("\n", "")
    separated_parts = line.split(" | ")
    unique_inputs = separated_parts[0].split(" ")
    output_values = separated_parts[1].split(" ")
    currentLine = []
    currentLine.append(unique_inputs)
    currentLine.append(output_values)
    fullOutput.append(currentLine)

print(fullOutput)
# is then copied to badOutput.txt
