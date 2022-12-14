with open('data_files/day_6.txt') as input_file:
    group_surveys = input_file.read().split('\n\n')

questions_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                  'u', 'v', 'w', 'x', 'y', 'z']
grand_total = 0

for group in group_surveys:
    for q in questions_list:
        if q in group:
            grand_total += 1
print(grand_total)

group_surveys = [group_survey.splitlines() for group_survey in group_surveys]

grand_total = 0
for group in group_surveys:
    for q in questions_list:
        if all([True if q in person else False for person in group]):
            grand_total += 1
print(grand_total)
