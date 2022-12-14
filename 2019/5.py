with open("data_files/day_5_input.txt") as input_file:
    input_string = input_file.read()
    raw_list = input_string.split(",")
    input_list = [int(num) for num in raw_list]

def find_number(n, par_count, op_code, int_list):
    if op_code:
        immediate_mode = op_code[0]
        op_code = op_code[1:]
    else:
        immediate_mode = '0'
        
    if immediate_mode == '1':
        par_value = int_list[n + par_count]
    else:
        par_index = int_list[n + par_count]
        par_value = int_list[par_index]

    return [par_value, op_code]

def iterate_program(int_list, input_number):
    n = 0

    while True:
        op_code = str(int_list[n])[::-1]
        instruction_id = op_code[0:2].replace("0", "")
        op_code = op_code[2:]

        if instruction_id == '99':
            break
        else:
            [first_number, op_code] = find_number(n, 1, op_code, int_list)
            [second_number, op_code] = find_number(n, 2, op_code, int_list)


        match instruction_id:
            case '1':
                target_index = int_list[n + 3]
                int_list[target_index] = first_number + second_number
                n += 4
                print(
                    "Addition performed:",
                    first_number,
                    "+",
                    second_number,
                    "at index",
                    target_index,
                    "resulting in",
                    int_list[target_index],
                )
            case "2":
                target_index = int_list[n + 3]
                int_list[target_index] = first_number * second_number
                n += 4
                print(
                    "Multiplication performed:",
                    first_number,
                    "*",
                    second_number,
                    "at index",
                    target_index,
                    "resulting in",
                    int_list[target_index],
                )
            case "3":
                target_index = int_list[n + 1]
                int_list[target_index] = input_number
                print("Set current input", input_number, "at index", target_index)
                n += 2
            case "4":
                output_number = first_number
                print("Outputting value", output_number, "from index", int_list[n + 1])
                n += 2
            case "5":
                print("Second number is", second_number)
                if first_number != 0:
                    n = second_number
                else:
                    n += 3
            case "6":
                if first_number == 0:
                    n = second_number
                else:
                    n += 3
            case "7":
                target_index = int_list[n + 3]
                if first_number < second_number:
                    int_list[target_index] = 1
                else:
                    int_list[target_index] = 0
                n += 4
            case "8":
                target_index = int_list[n + 3]
                if first_number == second_number:
                    int_list[target_index] = 1
                else:
                    int_list[target_index] = 0
                n += 4


iterate_program(input_list, 5)
