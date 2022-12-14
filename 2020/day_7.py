import re

digits_list = ['1', '2', '3', '4', '5', '6', '7', '8', '9']

with open('data_files/day_7.txt') as input_file:
    base_data = input_file.read().splitlines()
    bags_rules = [re.split(' 1 | 2 | 3 | 4 | 5 | 6 | 7 | 8 | 9 ', rule.replace(',', '').replace('.', '')) for rule in
                  base_data]
    bags_counts = [[int(n) for n in rule if n in digits_list] for rule in base_data]

bag_links = {}

for rule, count in zip(bags_rules, bags_counts):
    container_bag = rule[0][:-8]
    contained_bags = rule[1:]
    contained_bags_count = count
    bag_links[container_bag] = (contained_bags, count)

wanted_parents = ['shiny gold bags']
possible_parents = []

while wanted_parents:
    current_searched_parent = wanted_parents[0]
    wanted_parents.remove(current_searched_parent)
    for parent, sons in bag_links.items():
        if current_searched_parent in sons[0] or current_searched_parent[:-1] in sons[0]:
            wanted_parents.append(parent)
            possible_parents.append(parent)

# PART 2
# contained_bags = {'shiny gold bags': 1}
# wanted_bags = ['shiny gold bags']
#
# while wanted_bags:
#     print(wanted_bags[0])
#     current_bag = wanted_bags[0]
#     wanted_bags.remove(current_bag)
#     if not current_bag[-1] == 's':
#         current_bag += 's'
#
#     for parent, sons in bag_links.items():
#         if current_bag == parent or current_bag[:-1] == parent:
#             for son, count in zip(sons[0], sons[1]):
#                 try:
#                     if contained_bags.get(son):
#                         contained_bags[son] = int(contained_bags.get(parent) * count) + contained_bags.get(son)
#                     else:
#                         contained_bags[son] = int(contained_bags.get(parent) * count)
#                 except:
#                     if contained_bags.get(son):
#                         contained_bags[son] = int(contained_bags.get(parent[:-1]) * count) + contained_bags.get(son)
#                     else:
#                         contained_bags[son] = int(contained_bags.get(parent[:-1]) * count)
#
#                 wanted_bags.append(son)
#     print(contained_bags)

print(len(set(possible_parents)))
print(sum([value for (key, value) in contained_bags.items()]))
