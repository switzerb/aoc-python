from unittest import TestCase
import day12


class Test(TestCase):

    def test_p1_1(self):
        self.assertEqual(0, day12.part_one('#', ()))
        self.assertEqual(1, day12.part_one('.', ()))
        self.assertEqual(1, day12.part_one('???.###', (1, 1, 3)))

    def test_p1_2(self):
        self.assertEqual(4, day12.part_one('.??..??...?##.', (1, 1, 3)))

    def test_part_two(self):
        data = ""
        self.assertEqual(0, day12.part_two(data))
