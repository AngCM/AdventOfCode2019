import math


def calculate_required_fuel(mass):
    # divide by 3, round down, subtract 2
    return math.floor(mass/3) - 2


def calculate_total_required_fuel(mass):
    # calculate the fuel required to carry the fuel
    # divide by 3, round down, subtract 2
    mass = calculate_required_fuel(mass)
    if mass <= 8:
        return mass
    else:
        return mass + calculate_total_required_fuel(mass)


def main():
    # Day 1, Part 1: Find fuel requirements for modules
    # Part 2: find fuel requirements for modules and their fuel
    modules = open("day_1_input", "r")
    total_fuel_required = 0
    fuel_required = 0
    for module in modules:
        fuel_required += calculate_required_fuel(int(module))
        total_fuel_required += calculate_total_required_fuel(int(module))

    print(fuel_required)
    print(total_fuel_required)


if __name__ == "__main__":
    main()