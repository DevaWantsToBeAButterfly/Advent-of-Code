from string import ascii_letters

total_priority = 0
rucksack_index = 0

with open('.\data_files\day_3_input.txt') as input_file:
    rucksack_list = [line.replace('\n', '') for line in input_file ]
input_file.close()

for rucksack in rucksack_list:
    first_compartment = rucksack[:len(rucksack)//2]
    second_compartment = rucksack[len(rucksack)//2:]

    for item in first_compartment:
        if item in second_compartment:
            total_priority += ascii_letters.index(item) + 1
            break

print('The solution to part 1 is', total_priority)
total_priority = 0

while rucksack_index < len(rucksack_list):
    first_rucksack = rucksack_list[rucksack_index]
    second_rucksack = rucksack_list[rucksack_index + 1]
    third_rucksack = rucksack_list[rucksack_index + 2]

    for item in first_rucksack:
        if item in second_rucksack and item in third_rucksack:
            total_priority += ascii_letters.index(item) + 1
            break

    rucksack_index += 3

print('The solution to part 2 is', total_priority)
