def create_line_dictionary(array):
    line_coords = {}
    distance_traveled = 0
    x = 0
    y = 0

    for step in array:
        direction = step[0]
        distance = ''
        for i in range(1, len(step)):
            distance += step[i]
        distance = int(distance)

        for i in range(0, distance):
            distance_traveled += 1

            if direction == "U":
                y += 1
                current_location = (x, y)
                line_coords[current_location] = distance_traveled
            elif direction == "D":
                y -= 1
                current_location = (x, y)
                line_coords[current_location] = distance_traveled
            elif direction == "L":
                x -= 1
                current_location = (x, y)
                line_coords[current_location] = distance_traveled
            elif direction == "R":
                x += 1
                current_location = (x, y)
                line_coords[current_location] = distance_traveled
    return line_coords


def find_intersection(dict_1, dict_2):
    keys_1 = set(dict_1.keys())
    keys_2 = set(dict_2.keys())
    intersections = keys_1 & keys_2
    return intersections


def calculate_least_manhattan_distance(points):
    distances = []
    for point in points:
        distance = abs(point[0] - 0) + abs(point[1] - 0)
        distances.append(tuple((distance, point)))

    return min(distances)


def calculate_least_signal_delay(points, dict1, dict2):
    delays = []
    for point in points:
        delays.append(dict1[point] + dict2[point])
    return min(delays)


def main():
    # Day 3, part 1
    # Find the closest intersection of two wires
    file = open("day_3_input", "r")
    first = list(map(str, file.readline().strip().split(",")))
    second = list(map(str, file.readline().strip().split(",")))

    dict1 = create_line_dictionary(first)
    dict2 = create_line_dictionary(second)

    intersections = find_intersection(dict1, dict2)
    print(calculate_least_manhattan_distance(intersections))

    # Day 3, part 2
    # Find the shortest total traveled distance for an intersection of two wires
    print(calculate_least_signal_delay(intersections, dict1, dict2))


if __name__ == "__main__":
    main()
