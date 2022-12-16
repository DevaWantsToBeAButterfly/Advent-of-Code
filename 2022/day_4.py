from generic_functions import read_input

elf_pairs = read_input('.\data_files\day_4_input.txt')
elf_pairs = [(pair.split(',')[0].split('-'), pair.split(',')[1].split('-')) for pair in elf_pairs]
useless_elf_counter = 0
overlap_counter = 0

for pair in elf_pairs:
    first_elf_boundaries = [int(section) for section in pair[0]]
    second_elf_boundaries = [int(section) for section in pair[1]]
    first_elf_sections = set(range(first_elf_boundaries[0], first_elf_boundaries[1] + 1))
    second_elf_sections = set(range(second_elf_boundaries[0], second_elf_boundaries[1] + 1))
    overlapping_sections = first_elf_sections.intersection(second_elf_sections)

    if overlapping_sections:
        overlap_counter += 1

        if overlapping_sections == first_elf_sections or overlapping_sections == second_elf_sections:
            useless_elf_counter += 1

print(useless_elf_counter)
print(overlap_counter)
