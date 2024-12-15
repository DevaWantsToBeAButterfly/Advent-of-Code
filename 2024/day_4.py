from aocd import get_data, submit

letters = get_data(year=2024, day=4).splitlines()
letters = [list(row) for row in letters]
directions_offsets = {'up':[0, -1], 'down':[0, 1], 'left':[-1, 0], 'right':[1, 0],
                      'up-left':[-1, -1], 'up-right':[1, -1], 'down-left':[-1, 1], 'down-right':[1, 1]}

word_to_find = 'XMAS'
words_found = 0
crossings_found = 0

def find_xmas(direction, starting_position):
    current_position = starting_position
    found_word = 1

    for n in range(1, 4):
        current_position[0] += directions_offsets[direction][0]
        current_position[1] += directions_offsets[direction][1]
        if word_to_find[n] != letters[current_position[1]][current_position[0]]:
            found_word = 0
            break

    return found_word

def find_mas(letter_x, letter_y):
    letters_to_find = [['M', 'S'], ['M', 'S']]
    if letters[letter_y - 1][letter_x - 1] in letters_to_find[0]:
        letters_to_find[0].remove(letters[letter_y - 1][letter_x - 1])
        if letters[letter_y + 1][letter_x + 1] in letters_to_find[0]:
            if letters[letter_y - 1][letter_x + 1] in letters_to_find[1]:
                letters_to_find[1].remove(letters[letter_y - 1][letter_x + 1])
                if letters[letter_y + 1][letter_x - 1] in letters_to_find[1]:
                    return 1

    return 0

for y in range(len(letters)):
    for x in range(len(letters)):
        if letters[y][x] == 'X':
            if y >= 3:
                words_found += find_xmas('up', [x, y])

            if y <= (len(letters) - 4):
                words_found += find_xmas('down', [x, y])

            if x >= 3:
                words_found += find_xmas('left', [x, y])

            if x <= (len(letters[0]) - 4):
                words_found += find_xmas('right', [x, y])

            if y >= 3 and x >= 3 :
                words_found += find_xmas('up-left', [x, y])

            if y >= 3 and x <= (len(letters[0]) - 4) :
                words_found += find_xmas('up-right', [x, y])

            if y <= (len(letters) - 4) and x >= 3 :
                words_found += find_xmas('down-left', [x, y])

            if y <= (len(letters) - 4) and x <= (len(letters[0]) - 4) :
                words_found += find_xmas('down-right', [x, y])

        elif letters[y][x] == 'A':
            if 0 < y < len(letters) - 1 and 0 < x < len(letters[0]) - 1:
                crossings_found += find_mas(x, y)

submit(words_found, 'a')
submit(crossings_found, 'b')