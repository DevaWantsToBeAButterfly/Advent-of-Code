def read_lines(filepath):
    with open(filepath) as input_file:
        input_list = [line.replace('\n','') for line in input_file.readlines()]

    input_file.close()
    return input_list