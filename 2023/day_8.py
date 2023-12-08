from aocd import get_data, submit
import math

puzzle_input = get_data(year=2023, day=8).splitlines()

left_right_sequence = puzzle_input[0]
nodes = {line.split(' = ')[0]: line.split(' = ')[1].replace('(', '').replace(')', '').split(', ')
         for line in puzzle_input[2:]}

start_node = 'AAA'


def find_path_to_node(node, end_node):
    steps_taken = 0
    if len(end_node) == 3:
        while node != end_node:
            for step in left_right_sequence:
                steps_taken += 1
                if step == 'L':
                    node = nodes[node][0]
                else:
                    node = nodes[node][1]

    elif len(end_node) == 1:
        while node[-1] != end_node:
            for step in left_right_sequence:
                steps_taken += 1
                if step == 'L':
                    node = nodes[node][0]
                else:
                    node = nodes[node][1]

    return steps_taken


def find_primes(upper_limit):
    primes = []
    for n in range(2, upper_limit + 1):
        for div in range(2, int(n**0.5) + 1):
            if not n % div:
                break
        else:
            primes.append(n)

    return primes


def least_common_multiple(nums):
    factors_list = set()
    primes_list = find_primes(max(nums))
    for num in nums:
        while num >= 2:
            for div in primes_list:
                if not num % div:
                    factors_list.add(div)
                    num = num / div
                    break

    return math.prod(factors_list)


part_a_answer = find_path_to_node(start_node, 'ZZZ')
print(part_a_answer)
submit(part_a_answer, part='a')

start_nodes = [node for node in nodes if node[-1] == 'A']
steps_taken = []

for start_node in start_nodes:
    steps_taken.append(find_path_to_node(start_node, 'Z'))

part_b_answer = least_common_multiple(steps_taken)
print(part_b_answer)
submit(part_b_answer, part='b')
