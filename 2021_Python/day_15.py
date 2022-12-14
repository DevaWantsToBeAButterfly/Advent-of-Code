with open('data_files/day_15_input.txt') as input_file:
    base_dump = input_file.read().splitlines()
    ROW_LENGTH = len(base_dump[0])
    nodes_map = []
    for row in base_dump:
        row_list = [int(node) for node in row]
        nodes_map += row_list
    print(ROW_LENGTH, nodes_map)

nodes_list = [{'base_dist': num, 'total_dist': float('inf'), 'was_checked': False} for num in nodes_map]
id_num = 0
for node in nodes_list:
    node['id'] = id_num
    id_num += 1
nodes_list[0]['base_dist'] = 0
nodes_list[0]['total_dist'] = 0

while nodes_list[-1]['total_dist'] == float('inf'):
    unchecked_nodes = [node for node in nodes_list if not node['was_checked']]
    current_node = min(unchecked_nodes, key=lambda x: x['total_dist'])
    current_node['was_checked'] = True
    current_node_index = current_node['id']

    if current_node_index >= ROW_LENGTH:
        up_node = nodes_list[current_node_index - ROW_LENGTH]
        distance_from_current = current_node['total_dist'] + up_node['base_dist']
        if distance_from_current < up_node['total_dist']:
            up_node['total_dist'] = distance_from_current

    if current_node_index < len(nodes_list) - ROW_LENGTH:
        down_node = nodes_list[current_node_index + ROW_LENGTH]
        distance_from_current = current_node['total_dist'] + down_node['base_dist']
        if distance_from_current < down_node['total_dist']:
            down_node['total_dist'] = distance_from_current

    if current_node_index % ROW_LENGTH:
        left_node = nodes_list[current_node_index - 1]
        distance_from_current = current_node['total_dist'] + left_node['base_dist']
        if distance_from_current < left_node['total_dist']:
            left_node['total_dist'] = distance_from_current

    if (current_node_index + 1) % ROW_LENGTH:
        right_node = nodes_list[current_node_index + 1]
        distance_from_current = current_node['total_dist'] + right_node['base_dist']
        if distance_from_current < right_node['total_dist']:
            right_node['total_dist'] = distance_from_current

print(nodes_list[-1]['total_dist'])
