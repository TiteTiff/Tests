import unittest
import DigitToRoman

class DigitToRoman_test(unittest.TestCase):
    def test_one(self):
        self.assertEqual(DigitToRoman.DigitToRoman.int_one_to_roman(1), "I")

    def test_two(self):
        self.assertEqual(DigitToRoman.DigitToRoman.int_one_to_roman(2), "II")

    def test_three(self):
        self.assertEqual(DigitToRoman.DigitToRoman.int_one_to_roman(3), "III")
