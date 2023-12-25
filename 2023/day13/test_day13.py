from unittest import TestCase
import day13


class Test(TestCase):

    def test_part_one(self):
        rows = [
            ["#.##..##.",
             "..#.##.#.",
             "##......#",
             "##......#",
             "..#.##.#.",
             "..##..##.",
             "#.#.##.#."],

            ["#...##..#",
             "#....#..#",
             "..##..###",
             "#####.##.",
             "#####.##.",
             "..##..###",
             "#....#..#"],
        ]
        self.assertEqual(405, day13.part_one(rows))

    def test_part_two(self):
        data = ""
        self.assertEqual(0, day13.part_two(data))
