with open('data_files/day_5.txt') as input_file:
    boarding_passes = input_file.read().splitlines()

unique_seat_IDs = []
for boarding_pass in boarding_passes:
    lowest_row = 0
    highest_row = 127
    leftmost_column = 0
    rightmost_column = 7
    for char in boarding_pass:
        match char:
            case 'F':
                highest_row = (lowest_row + highest_row) // 2
            case 'B':
                lowest_row = (lowest_row + highest_row) // 2 + 1
            case 'L':
                rightmost_column = (leftmost_column + rightmost_column) // 2
            case 'R':
                leftmost_column = (leftmost_column + rightmost_column) // 2 + 1

    unique_seat_IDs.append(lowest_row * 8 + leftmost_column)

print(max(unique_seat_IDs))

for unique_id in range(min(unique_seat_IDs), max(unique_seat_IDs)):
    if unique_id not in unique_seat_IDs:
        print(unique_id)
