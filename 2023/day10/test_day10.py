from unittest import TestCase
import day10


class Test(TestCase):
    def test_p1_1(self):
        data = [
            ".....",
            ".S-7.",
            ".|.|.",
            ".L-J.",
            ".....",
        ]
        self.assertEqual(4, day10.part_one(day10.parse(data, "F")))

    def test_p1_2(self):
        data = [
            "-L|F7",
            "7S-7|",
            "L|7||",
            "-L-J|",
            "L|-JF",
        ]
        self.assertEqual(4, day10.part_one(day10.parse(data, "F")))

    def test_p2_1(self):
        data = [
            "..........",
            ".S------7.",
            ".|F----7|.",
            ".||OOOO||.",
            ".||OOOO||.",
            ".|L-7F-J|.",
            ".|II||II|.",
            ".L--JL--J.",
            "..........",
        ]
        self.assertEqual(4, day10.part_two(data))
