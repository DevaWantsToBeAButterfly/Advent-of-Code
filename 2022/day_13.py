from generic_functions import read_lines
from ast import literal_eval


pairs = read_lines('.\data_files\day_13_input.txt')
row_index = 0
pairs_correctness = []


def compare_packets(first_packet, second_packet):
    if not first_packet and not second_packet:
        return
    elif not first_packet:
        return 'right'
    elif not second_packet:
        return 'wrong'

    for el_index, first_packet_el in enumerate(first_packet):
        try:
            second_packet_el = second_packet[el_index]
        except IndexError:
            return 'wrong'

        if type(first_packet_el) == int:
            if type(second_packet_el) == int:
                if first_packet_el < second_packet_el:
                    return 'right'

                elif first_packet_el > second_packet_el:
                    return 'wrong'

            elif type(second_packet_el) == list:
                outcome = compare_packets([first_packet_el], second_packet_el)
                if outcome:
                    return outcome

        elif type(first_packet_el) == list:
            if type(second_packet_el) == list:
                outcome = compare_packets(first_packet_el, second_packet_el)
                if outcome:
                    return outcome
            elif type(second_packet_el) == int:
                outcome = compare_packets(first_packet_el, [second_packet_el])
                if outcome:
                    return outcome

    if len(first_packet) < len(second_packet):
        return 'right'


while row_index < len(pairs) - 1:
    first_pair = literal_eval(pairs[row_index])
    second_pair = literal_eval(pairs[row_index + 1])
    row_index += 3

    pairs_correctness.append(compare_packets(first_pair, second_pair))

total_sum = 0

for index, pair in enumerate(pairs_correctness):
    if pair == 'right':
        total_sum += index + 1

print(total_sum)

first_divider = [[2]]
second_divider = [[6]]
first_divider_index = 1
second_divider_index = 2 #First index is 1, plus 1 cuz [[2]] is added to the regular packets
for line in pairs:
    if line != '':
        if compare_packets(literal_eval(line), first_divider) == 'right':
            first_divider_index += 1

        if compare_packets(literal_eval(line), second_divider) == 'right':
            second_divider_index += 1

print(first_divider_index * second_divider_index)

