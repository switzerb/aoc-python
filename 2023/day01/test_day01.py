from unittest import TestCase
import day01


class Test(TestCase):
    def test_p1_1(self):
        inputs = [
            "1abc2",
            "pqr3stu8vwx",
            "a1b2c3d4e5f",
            "treb7uchet",
        ]
        self.assertEqual(142, day01.part_one(inputs))
