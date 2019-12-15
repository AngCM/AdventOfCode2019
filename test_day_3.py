import unittest
import day_3


class TestDay3(unittest.TestCase):
    first_wire = ("R75", "D30", "R83", "U83", "L12", "D49", "R71", "U7", "L72")
    second_wire = ("U62", "R66", "U55", "R34", "D71", "R55", "D58", "R83")

    def test_distance(self):
        dict_1 = day_3.create_line_dictionary(self.first_wire)
        dict_2 = day_3.create_line_dictionary(self.second_wire)
        intersections = day_3.find_intersection(dict_1, dict_2)
        distance = day_3.calculate_least_manhattan_distance(intersections)
        self.assertEqual(distance[0], 159)

    def test_steps(self):
        dict_1 = day_3.create_line_dictionary(self.first_wire)
        dict_2 = day_3.create_line_dictionary(self.second_wire)
        intersections = day_3.find_intersection(dict_1, dict_2)
        least_steps = day_3.calculate_least_signal_delay(intersections, dict_1, dict_2)
        self.assertEqual(least_steps, 610)


if __name__ == '__main__':
    unittest.main()
