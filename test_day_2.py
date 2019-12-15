import unittest
import day_2


class TestDay2(unittest.TestCase):
    def test_opcode_reader_first(self):
        first = day_2.read_opcodes([1,1,1,4,99,5,6,0,99])
        self.assertEqual(first, [30,1,1,4,2,5,6,0,99])
        self.assertEqual(first, [30,1,1,4,2,5,6,0,99])

    def test_opcode_reader_second(self):
        second = day_2.read_opcodes([1,0,0,0,99])
        self.assertEqual(second, [2,0,0,0,99])

    def test_opcode_reader_third(self):
        third = day_2.read_opcodes([2,4,4,5,99,0])
        self.assertEqual(third, [2,4,4,5,99,9801])

    def test_opcode_reader_fourth(self):
        fourth = day_2.read_opcodes([2,3,0,3,99])
        self.assertEqual(fourth, [2,3,0,6,99])


if __name__ == '__main__':
    unittest.main()
