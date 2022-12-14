with open('.\data_files\day_1_input.txt') as input_file:
    data = input_file.readlines()

current_elf_calories = 0
calories_totals = []

for line in data:
    if line != '\n':
        current_elf_calories += int(line)

    else:
        calories_totals.append(current_elf_calories)
        current_elf_calories = 0

print(max(calories_totals))
