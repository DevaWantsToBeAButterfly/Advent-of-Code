start_num = 172851
end_num = 675869


def always_increases(num):
    num = str(num)

    return list(num) == sorted(num)


def has_pair(num, part):
    num = str(num)
    if part == 1:
        if len(set(num)) < 6:
            return True
    else:
        for n in range(1, 10):
            n_count = num.count(str(n))
            if n_count == 2:
                return True


def find_codes(start_num, end_num, part):
    valid_codes = []
    for num in range(start_num, end_num + 1):
        if has_pair(num, part):
            if always_increases(num):
                valid_codes.append(num)

    return len(valid_codes)


print("Part 1 solution: " + str(find_codes(start_num, end_num, 1)))
print("Part 2 solution: " + str(find_codes(start_num, end_num, 2)))
