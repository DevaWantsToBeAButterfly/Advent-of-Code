from generic_functions import read_lines

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
words = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
numbers_and_words = numbers + words
words_to_nums = {'zero': '0', 'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6',
                 'seven': '7', 'eight': '8', 'nine': '9'}
running_total = 0

for line in read_lines('input_files/day_1.txt'):
    for char in line:
        if char in numbers:
            leftmost_num = char
            break
    for char in line[::-1]:
        if char in numbers:
            rightmost_num = char
            break

    running_total += int(leftmost_num + rightmost_num)

print(running_total)
running_total = 0

for line in read_lines('input_files/day_1.txt'):
    leftmost_num_index = 99999999
    leftmost_num = None
    rightmost_num_index = -1
    rightmost_num = None

    for num in numbers_and_words:
        if num in line:
            temp_leftmost_num_index = line.index(num)
            if temp_leftmost_num_index < leftmost_num_index:
                leftmost_num_index = line.index(num)
                leftmost_num = num

            temp_rightmost_num_index = line.rindex(num)
            if temp_rightmost_num_index > rightmost_num_index:
                rightmost_num_index = line.rindex(num)
                rightmost_num = num

    if leftmost_num in words:
        leftmost_num = words_to_nums[leftmost_num]
    if rightmost_num in words:
        rightmost_num = words_to_nums[rightmost_num]

    running_total += int(leftmost_num+rightmost_num)

print(running_total)