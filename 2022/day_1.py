with open('.\data_files\day_1_input.txt') as input_file:
    data = input_file.readlines()

input_file.close()

current_elf_calories = 0
calories_totals = []

for line in data:
    if line != '\n':
        current_elf_calories += int(line)

    else:
        calories_totals.append(current_elf_calories)
        current_elf_calories = 0

print('The Elf carrying the most calories has', max(calories_totals), 'calories')

calories_totals.sort(reverse=True)
top_three_elves_calories = calories_totals[0] + calories_totals[1] + calories_totals[2]
print('In total, the top three Elves are carrying', top_three_elves_calories, 'calories')
