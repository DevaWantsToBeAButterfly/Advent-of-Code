with open('data_files\day_10.txt') as input_file:
    data_list = [int(n) for n in input_file.readlines()]

current_connector = 0
one_diff_count = 0
three_diff_count = 1

while data_list:
    next_connector = min(data_list)
    if next_connector - current_connector == 1:
        one_diff_count += 1
    elif next_connector - current_connector == 3:
        three_diff_count += 1
    current_connector = next_connector
    data_list.remove(current_connector)

print(one_diff_count * three_diff_count)