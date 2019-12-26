from itertools import permutations


class Amplifier:
    def __init__(self, instructions):
        self.instructions = instructions
        for i in range(100000):
            self.instructions.append(0)
        #print(self.instructions)
        self.output = None
        self.position = 0
        self.saved_output = []
        self.relative_base = 0
        self.input = 2

    def run(self):
        self.saved_output = self.output

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
                return

            elif opcode == 1:
                self.instructions[self.write_position(self.instructions, self.instructions[p3], p3_mode)] = \
                    self.read_value(self.instructions, self.instructions[p1], p1_mode) + \
                    self.read_value(self.instructions, self.instructions[p2], p2_mode)
                self.position += 4

            elif opcode == 2:
                self.instructions[self.write_position(self.instructions, self.instructions[p3], p3_mode)] = \
                    self.read_value(self.instructions, self.instructions[p1], p1_mode) * \
                    self.read_value(self.instructions, self.instructions[p2], p2_mode)
                self.position += 4

            elif opcode == 3:
                # can now work in relative mode
                self.instructions[self.write_position(self.instructions, self.instructions[p1], p1_mode)] = self.input
                self.position += 2

            elif opcode == 4:
                self.output = self.read_value(self.instructions, self.instructions[p1], p1_mode)
                self.position += 2
                print('output is ', self.output)

            elif opcode == 5:
                if self.read_value(self.instructions, self.instructions[p1], p1_mode) != 0:
                    self.position = self.read_value(self.instructions, self.instructions[p2], p2_mode)
                else:
                    self.position += 3

            elif opcode == 6:
                if self.read_value(self.instructions, self.instructions[p1], p1_mode) == 0:
                    self.position = self.read_value(self.instructions, self.instructions[p2], p2_mode)
                else:
                    self.position += 3

            elif opcode == 7:
                if self.read_value(self.instructions, self.instructions[p1], p1_mode) < \
                        self.read_value(self.instructions, self.instructions[p2], p2_mode):
                    self.instructions[self.write_position(self.instructions, self.instructions[p3], p3_mode)] = 1
                else:
                    self.instructions[self.write_position(self.instructions, self.instructions[p3], p3_mode)] = 0
                self.position += 4

            elif opcode == 8:
                if self.read_value(self.instructions, self.instructions[p1], p1_mode) == \
                        self.read_value(self.instructions, self.instructions[p2], p2_mode):
                    self.instructions[self.write_position(self.instructions, self.instructions[p3], p3_mode)] = 1
                else:
                    self.instructions[self.write_position(self.instructions, self.instructions[p3], p3_mode)] = 0
                self.position += 4

            elif opcode == 9:
                # relative base offset
                self.relative_base += self.read_value(self.instructions, self.instructions[p1], p1_mode)
                self.position += 2

            else:
                print("Something went wrong, opcode: ", opcode, instruction)
                self.position += 4

    def read_value(self, instruction, position, mode):

        if int(mode) == 0:
            return instruction[position]
        elif int(mode) == 1:
            return position
        elif int(mode) == 2:
            return instruction[position + self.relative_base]
        else:
            print('error')

    def write_position(self, instruction, position, mode):

        if int(mode) == 0:
            return position
        elif int(mode) == 1:
            print('error, cannot write with mode 1')
        elif int(mode) == 2:
            return position + self.relative_base
        else:
            print('error')


def parse_intcode(instruction):
    intcode = list(str(instruction))
    # pad with 0s
    for i in range(0, (5-len(intcode))):
        intcode.insert(0, '0')
    return intcode


def main():
    file = open("day_9_input", "r")
    opcodes = list(map(int, file.read().split(",")))

    machine = Amplifier(opcodes[:])
    machine.run()


if __name__ == '__main__':
    main()
