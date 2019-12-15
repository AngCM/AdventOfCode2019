import unittest
import day_1


class TestDay1(unittest.TestCase):
    def test_module_fuel_required(self):
        self.assertEqual(day_1.calculate_required_fuel(1969), 654)

    def test_total_fuel_required(self):
        self.assertEqual(day_1.calculate_total_required_fuel(1969), 966)


if __name__ == '__main__':
    unittest.main()
