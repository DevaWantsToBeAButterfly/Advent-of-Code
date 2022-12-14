class IntcodeComputer:

    def __init__(self, instructions, print_output, user_input=None):
        if user_input is None:
            user_input = []
        self.original_instructions = instructions
        self.instructions = self.original_instructions.copy()
        self.instruction_pointer = 0
        self.user_input = user_input
        self.output = []
        self.relative_base = 0
        self.print_output = print_output

        while len(self.instructions) < 5000:
            self.instructions.append(0)

    def reset_memory(self):
        self.instructions = self.original_instructions.copy()
        self.instruction_pointer = 0
        self.output = []
        self.relative_base = 0

        while len(self.instructions) < 5000:
            self.instructions.append(0)

    def update_input(self, user_input):
        self.user_input = user_input
        self.reset_memory()

    def execute_program(self):
        while True:
            opcode = str(self.instructions[self.instruction_pointer])

            match opcode[-1]:
                case '1':
                    self.run_operation('sum', 2, opcode)

                case '2':
                    self.run_operation('product', 2, opcode)

                case '3':
                    self.run_operation('input', 0, opcode)

                case '4':
                    self.output.append(self.run_operation('output', 0, opcode))

                case '5':
                    self.run_operation('jump-if-true', 2, opcode)

                case '6':
                    self.run_operation('jump-if-false', 2, opcode)

                case '7':
                    self.run_operation('less-than', 2, opcode)

                case '8':
                    self.run_operation('equals', 2, opcode)

                case '9':
                    if opcode[-2:] == '99':
                        if self.print_output:
                            print(self.output)
                        return self.output

                    else:
                        self.run_operation('update-relative-base', 1, opcode)

    def run_operation(self, operation, parameters_count, opcode):
        opcode = opcode[::-1]
        opcode = opcode[2:]
        operation_parameters = []
        offset_from_pointer = 1

        while len(opcode) <= parameters_count:
            opcode += '0'

        for parameter_mode_id in opcode[:-1]:
            if parameter_mode_id == '0':
                parameter_address = self.instructions[self.instruction_pointer + offset_from_pointer]
                parameter_value = self.instructions[parameter_address]

            elif parameter_mode_id == '1':
                parameter_value = self.instructions[self.instruction_pointer + offset_from_pointer]

            elif parameter_mode_id == '2':
                parameter_address = self.instructions[self.instruction_pointer + offset_from_pointer] + \
                                    self.relative_base
                parameter_value = self.instructions[parameter_address]

            operation_parameters.append(parameter_value)
            offset_from_pointer += 1

        if operation in ['sum', 'product', 'jump-if-true', 'jump-if-false', 'less-than', 'equals',
                         'update-relative-base']:

            if operation == 'sum':
                try:
                    operation_result = operation_parameters[0] + operation_parameters[1]
                except:
                    print(operation_parameters)
                    quit()

            elif operation == 'product':
                operation_result = operation_parameters[0] * operation_parameters[1]

            elif operation == 'jump-if-true':
                if operation_parameters[0]:
                    self.instruction_pointer = operation_parameters[1]

                else:
                    self.instruction_pointer += (parameters_count + 1)

                return

            elif operation == 'jump-if-false':
                if not operation_parameters[0]:
                    self.instruction_pointer = operation_parameters[1]

                else:
                    self.instruction_pointer += (parameters_count + 1)

                return

            elif operation == 'less-than':
                if operation_parameters[0] < operation_parameters[1]:
                    operation_result = 1

                else:
                    operation_result = 0

            elif operation == 'equals':
                if operation_parameters[0] == operation_parameters[1]:
                    operation_result = 1

                else:
                    operation_result = 0

            elif operation == 'update-relative-base':
                self.relative_base += operation_parameters[0]
                self.instruction_pointer += (parameters_count + 1)
                return

        elif operation == 'input':
            operation_result = self.user_input[0]
            self.user_input = self.user_input[1:]

        elif operation == 'output':
            if opcode and opcode[0] == '1':
                output_value = self.instructions[self.instruction_pointer + offset_from_pointer]

            elif opcode and opcode[0] == '2':
                output_address = self.instructions[self.instruction_pointer + offset_from_pointer] + self.relative_base
                output_value = self.instructions[output_address]

            else:
                output_address = self.instructions[self.instruction_pointer + offset_from_pointer]
                output_value = self.instructions[output_address]

            self.instruction_pointer += (parameters_count + 2)
            return output_value

        if opcode[-1] == '0':
            operation_target_address = self.instructions[self.instruction_pointer + offset_from_pointer]

        elif opcode[-1] == '2':
            operation_target_address = self.instructions[self.instruction_pointer + offset_from_pointer] +\
                                       self.relative_base

        self.instructions[operation_target_address] = operation_result
        self.instruction_pointer += (parameters_count + 2)

    def search_inputs(self, wanted_output):

        for first_input in range(0, 100):
            for second_input in range(0, 100):
                self.reset_memory()
                self.instructions[1] = first_input
                self.instructions[2] = second_input
                self.execute_program()

                if self.instructions[0] == wanted_output:
                    print(first_input * 100 + second_input)
