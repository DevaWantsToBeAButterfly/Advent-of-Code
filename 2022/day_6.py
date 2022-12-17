from generic_functions import read_input

transmission = read_input('.\data_files\day_6_input.txt')
i = 0

while i < len(transmission):
    if len(set(transmission[i:i+4])) == 4:
        print(i + 4)
        break

    i += 1

i = 0

while i < len(transmission):
    if len(set(transmission[i:i+14])) == 14:
        print(i + 14)
        break

    i += 1
