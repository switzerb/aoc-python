import unittest
import day07


class DaySeven(unittest.TestCase):
    def test_p1_1(self):
        self.assertEqual(True, day07.contains_abba("abba"))

    def test_p1_2(self):
        self.assertEqual(True, day07.contains_abba("xyyxjump"))

    def test_p1_3(self):
        self.assertEqual(False, day07.contains_abba("aaaa"))

    def test_p1_4(self):
        self.assertEqual(True, day07.supports_tls("abba[mnop]qrst"))

    def test_p1_5(self):
        self.assertEqual(False, day07.supports_tls("abcd[bddb]xyyx"))

    def test_p1_6(self):
        self.assertEqual(False, day07.supports_tls("aaaa[qwer]tyui"))

    def test_p1_6(self):
        self.assertEqual(True, day07.supports_tls("ioxxoj[asdfgh]zxcvbn"))


if __name__ == '__main__':
    unittest.main()
