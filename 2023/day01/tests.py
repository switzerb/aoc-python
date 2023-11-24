import unittest

from day01.day01 import part_one, parse


class DayOne(unittest.TestCase):
    def test_p1_1(self):
        self.assertEqual(part_one(["R2", "L3"]), 5)  # add assertion here

    def test_p1_2(self):
        self.assertEqual(part_one(["R2", "R2", "R2"]), 2)  # add assertion here

    def test_p1_3(self):
        self.assertEqual(part_one(["R5", "L5", "R5", "R3"]), 12)

    def test_p1_actual(self):
        file = open("input.txt")
        self.assertEqual(part_one(parse(file.read())), 242)

if __name__ == '__main__':
    unittest.main()
