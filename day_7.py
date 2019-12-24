from itertools import permutations


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


def read_opcodes(array, input_list):
    i = 0
    running = True
    output = 0
    while running:
        instruction = parse_intcode(array[i])
        p1 = i+1
        p2 = i+2
        p3 = i+3
        p3_mode = instruction[0]
        p2_mode = instruction[1]
        p1_mode = instruction[2]
        opcode = int(instruction[3] + instruction[4])

        if opcode == 99:
            print('finished')
            running = False
            print('output was: ', output)
            return output

        elif opcode == 1:
            array[array[p3]] = parameter_value(array, array[p1], p1_mode) + parameter_value(array, array[p2], p2_mode)
            i += 4

        elif opcode == 2:
            array[array[p3]] = parameter_value(array, array[p1], p1_mode) * parameter_value(array, array[p2], p2_mode)
            i += 4

        elif opcode == 3:
            array[array[p1]] = input_list.pop()
            i += 2

        elif opcode == 4:
            output = parameter_value(array, array[p1], p1_mode)
            print(output)
            i += 2

        elif opcode == 5:
            if parameter_value(array, array[p1], p1_mode) != 0:
                i = parameter_value(array, array[p2], p2_mode)
            else:
                i += 3

        elif opcode == 6:
            if parameter_value(array, array[p1], p1_mode) == 0:
                i = parameter_value(array, array[p2], p2_mode)
            else:
                i += 3

        elif opcode == 7:
            if parameter_value(array, array[p1], p1_mode) < parameter_value(array, array[p2], p2_mode):
                array[array[p3]] = 1
            else:
                array[array[p3]] = 0
            i += 4

        elif opcode == 8:
            if parameter_value(array, array[p1], p1_mode) == parameter_value(array, array[p2], p2_mode):
                array[array[p3]] = 1
            else:
                array[array[p3]] = 0
            i += 4

        else:
            print("Something went wrong, opcode: ", opcode, instruction)
            i += 4


def main():
    file = open("day_7_input", "r")
    opcodes = list(map(int, file.read().split(",")))
    sequences = list(permutations([0, 1, 2, 3, 4]))

    max_signal = 0

    for sequence in sequences:
        amp_signal = 0
        input_list = []
        print('sequence is: ', sequence)
        for phase_signal in sequence:
            input_list.append(amp_signal)
            input_list.append(phase_signal)
            amp_signal = read_opcodes(opcodes, input_list)
        if amp_signal > max_signal:
            max_signal = amp_signal

    print('Max signal recieved was: ', max_signal)


if __name__ == '__main__':
    main()
