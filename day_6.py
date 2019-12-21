class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.children = []

    def set_parent(self, parent):
        self.parent = parent


def parse_orbit(orbit):
    # if XX)YY then YY is a child of XX
    return list(orbit.split(')'))


def create_tree(orbits):
    planets = {}

    for orbit in orbits:
        orbital_relationship = parse_orbit(orbit)
        if orbital_relationship[0] not in planets:
            planets[orbital_relationship[0]] = Node(orbital_relationship[0])
        if orbital_relationship[1] not in planets:
            planets[orbital_relationship[1]] = Node(orbital_relationship[1])

        planets[orbital_relationship[1]].set_parent(planets[orbital_relationship[0]])

    return planets


def calculate_total_orbits(planets):
    total = 0
    for planet in planets:
        current = planets[planet]
        while current.parent is not None:
            current = current.parent
            total += 1
    return total


def get_path_to_com(planet):
    path = []
    current = planet
    while current.parent is not None:
        path.append(current.data)
        current = current.parent
    path.append('COM')
    return path


def get_distance(path1, path2):
    diff1 = list(set(path1) - set(path2))
    diff2 = list(set(path2) - set(path1))
    return len(diff1) + len(diff2) - 2


def main():
    file = open("day_6_input", "r")
    orbits = list(map(str, file.read().split("\n")))

    planets = create_tree(orbits)
    print('Part 1 Answer: ', calculate_total_orbits(planets))

    san_path = get_path_to_com(planets['SAN'])
    you_path = get_path_to_com(planets['YOU'])

    path_distance = get_distance(san_path, you_path)
    print('Part 2 Answer: ', path_distance)


if __name__ == "__main__":
    main()
