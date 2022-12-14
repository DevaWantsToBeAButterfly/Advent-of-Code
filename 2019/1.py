import math


def read_input(fileDir):
    with open(fileDir) as input_text:
        input_list = input_text.readlines()

    return input_list


def calc_fuel(modules_list):
    needed_fuel = 0

    for module in modules_list:
        module = int(module)
        needed_fuel += math.floor(module / 3) - 2

    return needed_fuel


def calc_real_fuel(weight):
    fuel = math.floor(weight / 3) - 2

    if fuel >= 1:
        fuel += calc_real_fuel(fuel)

    else:
        fuel = 0

    return fuel


def find_total_fuel(modules_list):
    total_fuel = 0

    for module in modules_list:
        module = int(module)
        total_fuel += calc_real_fuel(module)

    return total_fuel


modules_list = read_input("day_1_input.txt")

fuel_cost = calc_fuel(modules_list)

print("Part 1 answer: " + str(fuel_cost))

real_fuel_cost = find_total_fuel(modules_list)

print("Part 2 answer: " + str(real_fuel_cost))
