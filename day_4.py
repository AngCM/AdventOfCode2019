from collections import Counter


def digits_increase(password):
    return sorted(password) == list(password)


def is_valid_password(password):
    # Password qualifications:
    # two adjacent digits are the same (repeating), but not part of a larger group
    # the digits never decrease left to right
    return digits_increase(password) and grouping_allowed(password)


def grouping_allowed(password):
    # use python Counter to keep track of digits
    digit_counter = Counter()
    for number in password:
        digit_counter[number] += 1

    # look for two adjacent digits that aren't part of a larger group
    return 2 in digit_counter.values()


def main():
    # range given by Advent of Code
    start_range = 134792
    end_range = 675810

    count_valid_passwords = 0

    for i in range(start_range, end_range + 1):
        if is_valid_password(str(i)):
            count_valid_passwords += 1
    print("Answer is: ", count_valid_passwords)


if __name__ == "__main__":
    main()

