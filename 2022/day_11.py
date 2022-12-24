from operator import add, mul
from generic_functions import read_lines


class Monkey:
    def __init__(self, starting_items, operation, divisibility_check, monkey_if_true, monkey_if_false):
        self.items = starting_items
        self.operation = operation
        self.divisibility_check = divisibility_check
        self.monkey_if_true = monkey_if_true
        self.monkey_if_false = monkey_if_false
        self.monkeys = []
        self.inspected_items = 0

    def update_items(self):
        for index, item in enumerate(self.items):
            self.inspected_items += 1

            if self.operation[1] == 'old':
                self.items[index] = do_maths(item, self.operation[0], item)
            else:
                self.items[index] = do_maths(item, self.operation[0], self.operation[1])

            if not self.items[index] % self.divisibility_check:
                self.monkeys[self.monkey_if_true].items.append(self.items[index])

            else:
                self.monkeys[self.monkey_if_false].items.append(self.items[index])

        self.items = []


def do_maths(left, operation, right):
    operation_result = operation(left, right) % (2*3*5*7*11*13*17*19)
    return operation_result


def input_parser(puzzle_input, monkey_list):
    for index, line in enumerate(puzzle_input):
        if line.startswith('M'):
            starting_items = puzzle_input[index + 1].split(': ')[1].split(', ')
            new_monkey_items = [int(item) for item in starting_items]

            operation_sign = puzzle_input[index + 2].split(' ')[-2]
            if operation_sign == '+':
                operation_sign = add
            elif operation_sign == '*':
                operation_sign = mul
            operation_num = puzzle_input[index + 2].split(' ')[-1]
            if operation_num != 'old':
                operation_num = int(operation_num)

            new_monkey_operation = (operation_sign, operation_num)

            new_monkey_div_check = int(puzzle_input[index + 3].split(' ')[-1])

            new_monkey_if_true = int(puzzle_input[index + 4].split(' ')[-1])
            new_monkey_if_false = int(puzzle_input[index + 5].split(' ')[-1])

            new_monkey = Monkey(new_monkey_items, new_monkey_operation, new_monkey_div_check, new_monkey_if_true,
                                new_monkey_if_false)

            monkey_list.append(new_monkey)

    for monkey in monkey_list:
        monkey.monkeys = monkey_list

    return monkey_list


puzzle_input = read_lines('./data_files/day_11_input.txt')
rounds_to_play = [20, 10000]

for count in rounds_to_play:
    monkey_list = input_parser(puzzle_input, [])

    for n in range(count):
        for monkey in monkey_list:
            monkey.update_items()

    inspected_items_counts = []
    for monkey in monkey_list:
        inspected_items_counts.append(monkey.inspected_items)

    inspected_items_counts.sort(reverse=True)
    print(inspected_items_counts[0]*inspected_items_counts[1])
    # Answer for part 1 is 58800
    # Answer for part 2 is 13937702909