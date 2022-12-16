from string import ascii_letters

total_priority = 0
rucksack_index = 0

with open('.\data_files\day_3_input.txt') as input_file:
    rucksack_list = [line.replace('\n', '') for line in input_file ]
input_file.close()

for rucksack in rucksack_list:
    first_compartment = set(rucksack[:len(rucksack)//2])
    second_compartment = set(rucksack[len(rucksack)//2:])
    common_item = list(first_compartment.intersection(second_compartment))[0]

    total_priority += ascii_letters.index(common_item) + 1

print('The solution to part 1 is', total_priority)
total_priority = 0

while rucksack_index < len(rucksack_list):
    first_rucksack = set(rucksack_list[rucksack_index])
    second_rucksack = set(rucksack_list[rucksack_index + 1])
    third_rucksack = set(rucksack_list[rucksack_index + 2])
    common_item = list(first_rucksack.intersection(second_rucksack.intersection(third_rucksack)))[0]
    
    total_priority += ascii_letters.index(common_item) + 1

    rucksack_index += 3

print('The solution to part 2 is', total_priority)
