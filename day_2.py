def read_opcodes(array):
    # Day 2, part 1
    for i in range(0, len(array), 4):
        if array[i] == 99:
            return array
        elif array[i] == 1:
            try:
                array[array[i+3]] = array[array[i+1]] + array[array[i+2]]
            except IndexError:
                print('Invalid Index')
        elif array[i] == 2:
            try:
                array[array[i+3]] = array[array[i+1]] * array[array[i+2]]
            except IndexError:
                print('Invalid Index')
        else:
            print("Something went wrong")
    print("Never hit 99...")


def find_opcode_noun_verb(opcodes, value):
    # day 2, part 2
    # find noun, verb that cause read_opcodes result[0] to be 19690720
    for noun in range(0, len(opcodes) - 1):
        for verb in range(0, len(opcodes) - 1):
            array = opcodes[:]
            array[1] = noun
            array[2] = verb
            result = read_opcodes(array)
            if result[0] == value:
                return noun, verb


def main():
    # Day 2, part 1
    # Note: before running the program, replace position 1 with the value 12 and replace position 2 with the value 2
    file = open("day_2_input", "r")
    opcodes = list(map(int, file.readline().split(",")))
    print(read_opcodes(opcodes)[0])

    # Day 2, part 2
    # find noun and verb (in positions 1 and 2) that cause program to output 19690720
    # answer should be in the form: 100 * noun + verb
    file = open("day_2_input", "r")
    opcodes = list(map(int, file.readline().split(",")))
    noun, verb = find_opcode_noun_verb(opcodes, 19690720)
    print(100 * noun + verb)


if __name__ == "__main__":
    main()
