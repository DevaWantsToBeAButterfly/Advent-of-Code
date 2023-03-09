with open('data_files\day_9.txt') as input_file:
    data_list = [int(n) for n in input_file.readlines()]
    preamble = data_list[:25].copy()
    composite_numbers = data_list[25:].copy()

for target_num in composite_numbers:
    found = False
    for first_n in preamble:
        second_n = target_num - first_n
        if second_n in preamble:
            preamble.pop(0)
            preamble.append(target_num)
            found = True
            break

    if not found:
        wanted_num = target_num
        print(wanted_num)
        break

for num_index, num in enumerate(data_list):
    nums = []
    for num_2 in data_list[num_index:]:
        nums.append(num_2)
        if sum(nums) > wanted_num:
            nums.pop(-1)
            break
    if sum(nums) == wanted_num and len(nums) > 1:
        print(min(nums) + max(nums))
        break