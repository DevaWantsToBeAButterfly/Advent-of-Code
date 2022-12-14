from math import prod

with open('data_files/day_9_input.txt') as input_file:
    data = input_file.read().splitlines()
    the_map = [[{'height': int(height), 'already_searched': False} for height in row] for row in data]

basins_sizes = []


def find_lowest_points(height_map):
    total_risk_level = 0
    for row_index, row in enumerate(height_map):
        for current_record_index, current_record in enumerate(row):
            current_record['x'] = current_record_index
            current_record['y'] = row_index
            current_record_height = current_record['height']
            records_to_check = [current_record_height]
            if row_index > 0:
                north_record = height_map[row_index - 1][current_record_index]
                records_to_check.append(north_record['height'])
            if row_index < len(height_map) - 1:
                south_record = height_map[row_index + 1][current_record_index]
                records_to_check.append(south_record['height'])
            if current_record_index > 0:
                west_record = height_map[row_index][current_record_index - 1]
                records_to_check.append(west_record['height'])
            if current_record_index < len(row) - 1:
                east_record = height_map[row_index][current_record_index + 1]
                records_to_check.append(east_record['height'])

            if min(records_to_check) == current_record_height and \
                    not max(records_to_check) == current_record_height:
                total_risk_level += (current_record_height + 1)

    print(total_risk_level)


def find_basins_loop(height_map):
    for row_index, row in enumerate(height_map):
        for current_record_index, current_record in enumerate(row):
            if not current_record['already_searched']:
                if not current_record['height'] == 9:
                    return explore_basin(current_record, height_map), True

    return height_map, False


def explore_basin(record, height_map):
    current_basin = [record]
    unchecked_records_in_basin = [record]

    while len(unchecked_records_in_basin):
        current_record = unchecked_records_in_basin[0]
        unchecked_records_in_basin.pop(0)
        current_record['already_searched'] = True
        row_index = current_record['y']
        col_index = current_record['x']

        if row_index > 0:
            north_record = height_map[row_index - 1][col_index]
            current_basin, unchecked_records_in_basin = check_if_record_in_basin(north_record, current_basin,
                                                                                 unchecked_records_in_basin)
        if row_index < len(height_map) - 1:
            south_record = height_map[row_index + 1][col_index]
            current_basin, unchecked_records_in_basin = check_if_record_in_basin(south_record, current_basin,
                                                                                 unchecked_records_in_basin)
        if col_index > 0:
            west_record = height_map[row_index][col_index - 1]
            current_basin, unchecked_records_in_basin = check_if_record_in_basin(west_record, current_basin,
                                                                                 unchecked_records_in_basin)
        if col_index < len(height_map[0]) - 1:
            east_record = height_map[row_index][col_index + 1]
            current_basin, unchecked_records_in_basin = check_if_record_in_basin(east_record, current_basin,
                                                                                 unchecked_records_in_basin)

    basins_sizes.append(len(current_basin))
    return height_map


def check_if_record_in_basin(record, basin, records_to_check):
    if not record['already_searched'] and not record['height'] == 9 and not record in basin:
        basin.append(record)
        records_to_check.append(record)

    return basin, records_to_check


find_lowest_points(the_map)

not_done = True
while not_done:
    the_map, not_done = find_basins_loop(the_map)

basins_sizes.sort(reverse=True)
print(prod(basins_sizes[:3]))
