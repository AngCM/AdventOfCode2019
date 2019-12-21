import unittest
import day_6


class TestDay6(unittest.TestCase):
    test_data = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L']
    part_2_data = ['COM)B', 'B)C', 'C)D', 'D)E', 'E)F', 'B)G', 'G)H', 'D)I', 'E)J', 'J)K', 'K)L', 'K)YOU', 'I)SAN']

    def test_orbit_count(self):
        orbits = self.test_data
        planets = day_6.create_tree(orbits)
        count = day_6.calculate_total_orbits(planets)
        self.assertEqual(count, 42)

    def test_route_distance(self):
        orbits = self.part_2_data
        planets = day_6.create_tree(orbits)
        san_path = day_6.get_path_to_com(planets['SAN'])
        you_path = day_6.get_path_to_com(planets['YOU'])

        path_distance = day_6.get_distance(san_path, you_path)
        self.assertEqual(path_distance, 4)