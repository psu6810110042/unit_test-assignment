import unittest
from _6810110042.stair_case import staircase


class StaircaseTest(unittest.TestCase):
    def test_give_2_with_hash_should_be_hh(self):
        # arrange
        n = 2
        pattern = "#"
        expected_output = " #\n##"

        # act
        result = staircase(n, pattern)

        # assert
        self.assertEqual(result, expected_output, f"Should be:\n{expected_output}")

    def test_give_4_with_hash(self):
        n = 4
        expected_output = "   #\n  ##\n ###\n####"
        result = staircase(n)  # Testing the default pattern
        self.assertEqual(result, expected_output)

    def test_give_3_with_asterisk(self):
        n = 3
        pattern = "*"
        expected_output = "  *\n **\n***"
        result = staircase(n, pattern)
        self.assertEqual(result, expected_output)

    def test_give_1(self):
        n = 1
        expected_output = "#"
        result = staircase(n)
        self.assertEqual(result, expected_output)

    def test_give_0_returns_empty_string(self):
        n = 0
        expected_output = ""
        result = staircase(n)
        self.assertEqual(result, expected_output)
