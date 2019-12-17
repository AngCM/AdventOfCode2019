import unittest
import day_4


class TestDay4(unittest.TestCase):
    def test_passwords_1(self):
        self.assertEqual(day_4.is_valid_password('112222'), True)

    def test_passwords_2(self):
        self.assertEqual(day_4.is_valid_password('123444'), False)

    def test_passwords_3(self):
        self.assertEqual(day_4.is_valid_password('119980'), False)

    def test_passwords_4(self):
        self.assertEqual(day_4.is_valid_password('112345'), True)

    def test_passwords_5(self):
        self.assertEqual(day_4.is_valid_password('111122'), True)


if __name__ == '__main__':
    unittest.main()
