from aocd import get_data, submit
import math

puzzle_data = get_data(year=2024, day=5).split('\n\n')
page_pairs = puzzle_data[0].splitlines()
page_sequences = puzzle_data[1].splitlines()

pages = {}

def recursive_downgrade(child, parent):
    pages[child][0] = min(pages[child][0] - 1, pages[parent][0] - 1)
    for super_child in pages[child][1]:
        recursive_downgrade(super_child, child)

for pair in page_pairs:
    first_page = pair.split('|')[0]
    second_page = pair.split('|')[1]
    if second_page not in pages:
        pages[second_page] = [100, [first_page]]
    else:
        pages[second_page][1].append(pair.split('|')[0])

    if first_page not in pages:
        pages[first_page] = [pages[second_page][0] - 1, []]
    else:
        pages[first_page][0] = min(pages[first_page][0] - 1, pages[second_page][0] - 1)

        for page in pages[first_page][1]:
            recursive_downgrade(page, first_page)
            pages[page][0] = min(pages[page][0] - 1, pages[first_page][0] - 1)

middles= 0

for y in pages:
    print(y[0])

for ordering in page_sequences:
    page_list = ordering.split(',')
    print(page_list)
    is_ordered = True
    for n in range(len(page_list) - 1):
        for x in range(n + 1, len(page_list)):
            if pages[page_list[n]][0] > pages[page_list[x]][0]:
                is_ordered = False
                break
    if is_ordered:
        middles += int(page_list[math.floor(len(page_list)/2)])

print(middles)
submit(middles, 'a')