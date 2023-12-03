from unittest import TestCase
import day03


class Test(TestCase):

    def test_part_one(self):
        schematic = """
467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""
        self.assertEqual(4361, day03.part_one(schematic))

    def test_part_two(self):
        data = ""
        self.assertEqual(0, day03.part_two(data))
