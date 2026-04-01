import unittest

import DigitToRoman


class DigitToRoman_test(unittest.TestCase):
    def test_one(self):
        self.assertEqual(DigitToRoman.DigitToRoman.int_to_roman(1), "I")

    def test_two(self):
        self.assertEqual(DigitToRoman.DigitToRoman.int_to_roman(2), "II")

    def test_three(self):
        self.assertEqual(DigitToRoman.DigitToRoman.int_to_roman(3), "III")

    def test_four(self):
        self.assertEqual(DigitToRoman.DigitToRoman.int_to_roman(4), "IV")

    def test_max_number(self):
        self.assertEqual(DigitToRoman.DigitToRoman.int_to_roman(3999), "MMMCMXCIX")

    def test_forty_nine(self):
        self.assertEqual(DigitToRoman.DigitToRoman.int_to_roman(49), "XLIX")