with open('data_files/day_2.txt') as input_file:
    passwords = [{'rule': line[:line.index(':')], 'password': line[line.index(':') + 2:]} for line in
                 input_file.read().splitlines()]


def solve(part):
    valid_passwords = 0

    for password_info in passwords:
        password_value = password_info['password']
        password_rule = password_info['rule']
        rule_letter = password_info['rule'][-1]
        first_rule_num = int(password_rule[:password_rule.index('-')])
        second_rule_num = int(password_rule[password_rule.index('-') + 1:password_rule.index(' ')])

        if part == 1:
            if password_value.count(rule_letter) in range(first_rule_num, second_rule_num + 1):
                valid_passwords += 1
        elif part == 2:
            if (password_value[first_rule_num - 1] == rule_letter) != (
                    password_value[second_rule_num - 1] == rule_letter):
                valid_passwords += 1

    print(valid_passwords)


solve(1)
solve(2)
