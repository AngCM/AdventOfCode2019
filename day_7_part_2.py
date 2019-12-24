from itertools import permutations


class Amplifier:
    def __init__(self, instructions, input_signals):

        self.input_signals = input_signals
        self.instructions = instructions
        self.state = 'Paused'
        self.output = []
        self.position = 0
        self.saved_output = []

    def run(self, input):
        self.saved_output = self.output[:]
        if self.state != 'Off':
            self.output = []
        self.input_signals = self.input_signals + input

        while True:
            instruction = parse_intcode(self.instructions[self.position])
            p1 = self.position + 1
            p2 = self.position + 2
            p3 = self.position + 3
            p3_mode = instruction[0]
            p2_mode = instruction[1]
            p1_mode = instruction[2]
            opcode = int(instruction[3] + instruction[4])

            if opcode == 99:
                self.state = 'Off'
                return

            elif opcode == 1:
                self.instructions[self.instructions[p3]] = \
                    parameter_value(self.instructions, self.instructions[p1], p1_mode) + \
                    parameter_value(self.instructions, self.instructions[p2], p2_mode)
                self.position += 4

            elif opcode == 2:
                self.instructions[self.instructions[p3]] = \
                    parameter_value(self.instructions, self.instructions[p1], p1_mode) * \
                    parameter_value(self.instructions, self.instructions[p2], p2_mode)
                self.position += 4

            elif opcode == 3:
                # must block here
                if len(self.input_signals) != 0:
                    self.state = 'Locked'
                    self.instructions[self.instructions[p1]] = self.input_signals.pop(0)
                    self.position += 2
                else:
                    print('3 output is: ', self.output)
                    return

            elif opcode == 4:
                self.output.append(parameter_value(self.instructions, self.instructions[p1], p1_mode))
                self.position += 2
                return

            elif opcode == 5:
                if parameter_value(self.instructions, self.instructions[p1], p1_mode) != 0:
                    self.position = parameter_value(self.instructions, self.instructions[p2], p2_mode)
                else:
                    self.position += 3

            elif opcode == 6:
                if parameter_value(self.instructions, self.instructions[p1], p1_mode) == 0:
                    self.position = parameter_value(self.instructions, self.instructions[p2], p2_mode)
                else:
                    self.position += 3

            elif opcode == 7:
                if parameter_value(self.instructions, self.instructions[p1], p1_mode) < \
                        parameter_value(self.instructions, self.instructions[p2], p2_mode):
                    self.instructions[self.instructions[p3]] = 1
                else:
                    self.instructions[self.instructions[p3]] = 0
                self.position += 4

            elif opcode == 8:
                if parameter_value(self.instructions, self.instructions[p1], p1_mode) == \
                        parameter_value(self.instructions, self.instructions[p2], p2_mode):
                    self.instructions[self.instructions[p3]] = 1
                else:
                    self.instructions[self.instructions[p3]] = 0
                self.position += 4

            else:
                print("Something went wrong, opcode: ", opcode, instruction)
                self.position += 4


def parameter_value(instruction, position, mode):
    if int(mode) == 0:
        return instruction[position]
    elif int(mode) == 1:
        return position
    else:
        print('error')


def parse_intcode(instruction):
    intcode = list(str(instruction))
    # pad with 0s
    for i in range(0, (5-len(intcode))):
        intcode.insert(0, '0')
    return intcode


def main():
    file = open("day_7_input", "r")
    opcodes = list(map(int, file.read().split(",")))
    sequences = list(permutations([5, 6, 7, 8, 9]))
    all_outputs = []

    for sequence in sequences:
        ampA = Amplifier(opcodes[:], [sequence[0], 0]) # first input is 0
        ampB = Amplifier(opcodes[:], [sequence[1]])
        ampC = Amplifier(opcodes[:], [sequence[2]])
        ampD = Amplifier(opcodes[:], [sequence[3]])
        ampE = Amplifier(opcodes[:], [sequence[4]])

        while ampE.state != 'Off':
            ampA.run(ampE.output)
            ampB.run(ampA.output)
            ampC.run(ampB.output)
            ampD.run(ampC.output)
            ampE.run(ampD.output)

        all_outputs.append(ampE.saved_output.pop(0))

    print('Answer is: ', max(all_outputs))


if __name__ == '__main__':
    main()
