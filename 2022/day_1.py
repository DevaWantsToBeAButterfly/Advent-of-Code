with open('.\data_files\day_1_input.txt') as input_file:
    calories_list = [int(line) if line != '\n' else 0 for line in input_file.readlines()]

input_file.close()

current_elf_calories = 0
elves_calorie_totals = []

for line in calories_list:
    if line:
        current_elf_calories += line

    else:
        elves_calorie_totals.append(current_elf_calories)
        current_elf_calories = 0

elves_calorie_totals.sort(reverse=True)

print('The Elf carrying the most calories has', elves_calorie_totals[0], 'calories')
print('In total, the top three Elves are carrying', sum(elves_calorie_totals[0:3]), 'calories')
