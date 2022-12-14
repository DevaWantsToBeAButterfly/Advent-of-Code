with open('data_files/day_4.txt') as input_file:
    passports = [line.replace('\n', ' ').split(' ') for line in input_file.read().split('\n\n')]
    passports = [{field.split(':')[0]: field.split(':')[1] for field in passport} for passport in passports]

valid_hair_color_bits = ['a', 'b', 'c', 'd', 'e', 'f', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
valid_eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
valid_passports = []
for passport in passports:
    if len(passport.items()) == 8 or (len(passport.items()) == 7 and not passport.get('cid')):
        valid_passports.append(passport)
print(len(valid_passports))
actually_valid_passports = 0
for passport in valid_passports:
    if int(passport.get('byr')) in range(1920, 2003):
        if int(passport.get('iyr')) in range(2010, 2021):
            if int(passport.get('eyr')) in range(2020, 2031):
                if (passport.get('hgt')[2:] == 'in' and int(passport.get('hgt')[:2]) in range(59, 77)) or (
                        passport.get('hgt')[3:] == 'cm' and int(passport.get('hgt')[:3]) in range(150, 194)):
                    if passport.get('hcl')[0] == '#' and all(
                            [True for char in passport.get('hcl')[1:] if char in valid_hair_color_bits]):
                        if passport.get('ecl') in valid_eye_colors:
                            if len(passport.get('pid')) == 9:
                                actually_valid_passports += 1

print(actually_valid_passports)
