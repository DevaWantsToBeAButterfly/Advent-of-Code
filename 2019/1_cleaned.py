with open('data_files/day_1_input.txt') as input_file:
    modules_list = [int(module) for module in input_file.readlines()]


def calc_total_fuel(modules, mode):
    if mode == 'Part 1':
        return sum([(module // 3 - 2) for module in modules])
    elif mode == 'Part 2':
        return sum([recurse_module_fuel(module) for module in modules])


def recurse_module_fuel(weight):
    fuel_cost = weight // 3 - 2

    if fuel_cost > 0:
        fuel_cost += recurse_module_fuel(fuel_cost)
    else:
        fuel_cost = 0

    return fuel_cost


print(f'Part 1 solution: {calc_total_fuel(modules_list, "Part 1")}')
print(f'Part 2 solution: {calc_total_fuel(modules_list, "Part 2")}')
