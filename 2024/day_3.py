from aocd import get_data, submit, puzzle

puzzle_data = get_data(year=2024, day=3)

numbers = ['0','1','2','3','4','5','6','7','8','9']


def parse_input(input_data, check_if_enabled):
    running_total = 0
    mul_enabled = True

    for n in range(len(input_data)):
        if check_if_enabled:
            if input_data[n:n+7] == "don't()":
                mul_enabled = False
            elif input_data[n:n+4] == "do()":
                mul_enabled = True

        if input_data[n:n+4] == 'mul(' and mul_enabled:
            first_number = ''
            second_number = ''
            offset = 4
            first_number_is_full = False
            correct_instruction = False

            while True:
                current_char = input_data[n+offset]

                if current_char == ',' and not first_number_is_full:
                    first_number_is_full = True
                elif current_char == ')' and first_number and second_number:
                    correct_instruction = True
                    break
                elif current_char in numbers:
                    if first_number_is_full:
                        second_number += current_char
                    else:
                        first_number += current_char
                else:
                    break

                offset += 1

            if correct_instruction:
                running_total += (int(first_number) * int(second_number))

    return running_total

submit(parse_input(puzzle_data, False), 'a')
submit(parse_input(puzzle_data, True), 'b')