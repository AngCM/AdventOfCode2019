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
    if len(intcode) < 5:
        for i in range(0, (5-len(intcode))):
            intcode.insert(0, '0')
    return intcode


def read_opcodes(array):
    input = 1

    i = 0
    while array[i] != 99:
        instruction = parse_intcode(array[i])
        p1 = i+1
        p2 = i+2
        p3 = i+3
        p3_mode = instruction[0]
        p2_mode = instruction[1]
        p1_mode = instruction[2]
        opcode = int(str(instruction[3]) + str(instruction[4]))

        if opcode == 99:
            print('finished')
            return

        elif opcode == 1:
            array[array[p3]] = parameter_value(array, array[p1], p1_mode) + parameter_value(array, array[p2], p2_mode)
            i += 4

        elif opcode == 2:
            array[array[p3]] = parameter_value(array, array[p1], p1_mode) * parameter_value(array, array[p2], p2_mode)
            i += 4

        elif opcode == 3:
            array[array[p1]] = input
            i += 2 

        elif opcode == 4:
            print(array[array[p1]])
            i += 2

        else:

            print("Something went wrong")
            i += 4


def main():
    file = open("day_5_input", "r")
    opcodes = list(map(int, file.read().split(",")))
    read_opcodes(opcodes)


if __name__ == '__main__':
    main()