with open('data_files/day_3.txt') as input_file:
    trees_map = input_file.read().splitlines()


def solve(right_movement, down_movement):
    trees_hit = 0
    for row_index, row in enumerate(trees_map):
        if not row_index % down_movement:
            current_spot_index = row_index * right_movement // down_movement
            if current_spot_index >= len(row):
                current_spot_index %= len(row)

            if row[current_spot_index] == '#':
                trees_hit += 1
    return trees_hit


print(solve(3, 1))
print(solve(1, 1) * solve(3, 1) * solve(5, 1) * solve(7, 1) * solve(1, 2))
