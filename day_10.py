from math import atan2


def adjust_origin(origin, asteroid):
    x = asteroid[0] - origin[0]
    y = asteroid[1] - origin[1]
    coord = (x, y)
    return coord


def find_max_visible(data):
    max_visible = 0
    for potential_base in data.values():
        if len(set(potential_base)) > max_visible:
            max_visible = len(set(potential_base))
    return max_visible


def asteroid_distances(data):
    for potential_base in data:
        asteroids = []
        data[potential_base] = list(data.keys())

        for asteroid in data[potential_base]:
            if asteroid != potential_base:
                asteroid = adjust_origin(potential_base, asteroid)
                asteroids.append((atan2(asteroid[1], asteroid[0])))
        data[potential_base] = asteroids
    return data


def parse_input(file_name):
    file = open(file_name, "r")
    data = {}
    for y, line in enumerate(file):
        for x in range(0, len(line.strip())):
            if line[x] == '#':
                coord = (x, y)
                symbol = list(map(str, line.strip()))
                data[coord] = symbol[x]
    return data


def main():
    data = parse_input('day_10_input')
    neighbors = asteroid_distances(data)

    print(find_max_visible(neighbors))


if __name__ == '__main__':
    main()