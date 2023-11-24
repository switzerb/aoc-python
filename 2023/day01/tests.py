import unittest
from day01.day01 import part_one


class DayOne(unittest.TestCase):
    def test_partOne(self):
        input = ["R2", "L3"]
        self.assertEqual(part_one(input), 5)  # add assertion here


if __name__ == '__main__':
    unittest.main()
