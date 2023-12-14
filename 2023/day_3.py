from aocd import get_data, submit

puzzle_input = get_data(year=2023, day=3).splitlines()
engine_map = [list(row) for row in puzzle_input]
numbers = '0123456789'
