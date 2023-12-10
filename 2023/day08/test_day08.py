from unittest import TestCase
import day08


class Test(TestCase):

    def test_p1_1(self):
        data = (
            "RL",
            {
                "AAA": ("BBB", "CCC"),
                "BBB": ("DDD", "EEE"),
                "CCC": ("ZZZ", "GGG"),
                "DDD": ("DDD", "DDD"),
                "EEE": ("EEE", "EEE"),
                "GGG": ("GGG", "GGG"),
                "ZZZ": ("ZZZ", "ZZZ"),
            }
        )
        self.assertEqual(2, day08.part_one(data))

    def test_p1_2(self):
        data = (
            "LLR",
            {
                "AAA": ("BBB", "BBB"),
                "BBB": ("AAA", "ZZZ"),
                "ZZZ": ("ZZZ", "ZZZ"),
            }
        )
        self.assertEqual(6, day08.part_one(data))

    def test_part_two(self):
        data = ""
        self.assertEqual(0, day08.part_two(data))
