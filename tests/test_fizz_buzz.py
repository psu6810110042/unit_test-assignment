from _6810110042.fizz_buzz import fizz_buzz
import unittest


class FizzBuzzTest(unittest.TestCase):
    def test_divisible_by_15(self):
        self.assertEqual(fizz_buzz(15), "FizzBuzz")
        self.assertEqual(fizz_buzz(30), "FizzBuzz")

    def test_divisible_by_3_only(self):
        self.assertEqual(fizz_buzz(3), "Fizz")
        self.assertEqual(fizz_buzz(6), "Fizz")
        self.assertEqual(fizz_buzz(9), "Fizz")

    def test_divisible_by_5_only(self):
        self.assertEqual(fizz_buzz(5), "Buzz")
        self.assertEqual(fizz_buzz(10), "Buzz")
        self.assertEqual(fizz_buzz(20), "Buzz")

    def test_regular_numbers_return_none(self):
        self.assertIsNone(fizz_buzz(1))
        self.assertIsNone(fizz_buzz(2))
        self.assertIsNone(fizz_buzz(7))

    def test_zero_and_negatives(self):
        self.assertEqual(fizz_buzz(0), "FizzBuzz")
        self.assertEqual(fizz_buzz(-3), "Fizz")
