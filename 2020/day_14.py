from aocd import get_data, submit

puzzle_input = get_data(day=14, year=2020)


def translate_to_binary(num):
    as_binary = ''
    while num:
        as_binary += str(num % 2)
        num = num // 2

    print(as_binary[::-1])

