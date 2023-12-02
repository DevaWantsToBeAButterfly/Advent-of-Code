from aocd import get_data, submit

input_data = get_data(year=2018).splitlines()
double_letters = 0
triple_letters = 0

for box_id in input_data:
    double_letter_in_id = False
    triple_letter_in_id = False
    checked_letters = set()

    for letter in box_id:
        if letter not in checked_letters:
            if box_id.count(letter) == 2:
                double_letter_in_id = True
            elif box_id.count(letter) == 3:
                triple_letter_in_id = True

            checked_letters.add(letter)

    if double_letter_in_id:
        double_letters += 1
    if triple_letter_in_id:
        triple_letters += 1

print(double_letters * triple_letters)
submit(double_letters * triple_letters, part='a')

box_ids_set = set()
for box_id in input_data:
    box_ids_set.add(box_id)
    for past_box_id in box_ids_set:
        differing_letters = 0
        letter_i = 0
        while letter_i < len(box_id) and differing_letters < 2:
            if box_id[letter_i] != past_box_id[letter_i]:
                differing_letters += 1
                differing_letter_index = letter_i
            letter_i += 1

        if differing_letters == 1:
            print(box_id[:differing_letter_index] + box_id[differing_letter_index + 1:])
            submit(box_id[:differing_letter_index] + box_id[differing_letter_index + 1:], part='b')
