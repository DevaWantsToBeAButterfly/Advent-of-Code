import math, time
from aocd import get_data, submit

puzzle_input = get_data(year=2024, day=7)
test_input = """190: 10 19
3267: 81 40 27
83: 17 5
156: 15 6
7290: 6 8 6 15
161011: 16 10 13
192: 17 8 14
21037: 9 7 18 13
292: 11 6 16 20"""

start_time = time.time()

def convert_to_binary(number, needed_length):
    as_binary = ''
    while number >= 1:
        as_binary += str(number % 3)
        number = math.floor(number / 3)

    while len(as_binary) < needed_length:
        as_binary += '0'
    return as_binary[::-1]

total_correct_results = 0

for line in puzzle_input.splitlines():
    line = line.split(': ')
    target = int(line[0])
    factors = [int(num) for num in line[1].split(' ')]
    operations = len(factors) - 1
    possible_permutations = 3**operations
    results_found = set()

    for n in range(possible_permutations):
        current_factors = [n for n in factors]
        current_step = 0
        first_factor = None
        second_factor = None
        operations_permutation = convert_to_binary(n, operations)

        while True:
            if not first_factor:
                first_factor = current_factors[0]
                second_factor = current_factors[1]
                current_factors.pop(0)
                current_factors.pop(0)
            else:
                second_factor = current_factors[0]
                current_factors.pop(0)

            if int(operations_permutation[current_step]) == 0:
                first_factor = first_factor + second_factor
            elif int(operations_permutation[current_step]) == 1:
                first_factor = first_factor * second_factor
            else:
                first_factor = int(str(first_factor) + str(second_factor))

            current_step += 1
            if not current_factors:
                break

        results_found.add(first_factor)

    if target in results_found:
        total_correct_results += target

print("--- %s seconds ---" % (time.time() - start_time))
submit(total_correct_results, 'b')