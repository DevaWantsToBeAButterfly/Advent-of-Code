from collections import Counter

with open('data_files/day_3_input.txt') as input_file:
    diagnostic_report = input_file.read().splitlines()

# ----PART 1----
gamma_rate = ''

for bit_i in range(len(diagnostic_report[0])):
    bit_count = Counter(binary_num[bit_i] for binary_num in diagnostic_report)
    gamma_rate += bit_count.most_common(1)[0][0]

epsilon_rate = ''.join(['0' if bit == '1' else '1' for bit in gamma_rate])

print(f"The submarine's power consumption is {int(gamma_rate, 2) * int(epsilon_rate, 2)}")


# ---- PART 2----
def find_correct_binary(report, criteria):
    if criteria == 'most_common':
        target_index = 0
        target_value = '1'
    else:
        target_index = -1
        target_value = '0'

    while len(report) > 1:
        for bit_index in range(len(report[0])):
            bit_counter = Counter(binary_num[bit_index] for binary_num in report)
            correct_bit = bit_counter.most_common()[target_index]
            if correct_bit[1] == len(report) / 2:
                correct_bit = target_value
            else:
                correct_bit = correct_bit[0]
            report = [binary_num for binary_num in report if binary_num[bit_index] == correct_bit]

    return report[0]


oxygen_generator_rating = find_correct_binary(diagnostic_report, 'most_common')
CO2_scrubber_rating = find_correct_binary(diagnostic_report, 'least_common')

print(f"The submarine's life support rating is {int(oxygen_generator_rating, 2) * int(CO2_scrubber_rating, 2)}")
