with open('data_files/day_1.txt') as input_file:
    entries_list = [int(entry) for entry in input_file.readlines()]


def solve(part: int):
    for first_entry_index, first_entry in enumerate(entries_list):
        for second_entry in entries_list[first_entry_index + 1:]:
            if part == 1:
                if first_entry + second_entry == 2020:
                    return f'The solution for part 1 is {first_entry * second_entry}'

            elif part == 2:
                for third_entry in entries_list[first_entry_index + 2:]:
                    if first_entry + second_entry + third_entry == 2020:
                        return f'The solution for part 2 is {first_entry * second_entry * third_entry}'


print(solve(1))
print(solve(2))
