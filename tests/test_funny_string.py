from _6810110042.funny_string import funnyString
import unittest


class FunnyStringTest(unittest.TestCase):
    def test_acxz_is_funny(self):
        # arrange
        s = "acxz"
        expected_output = "Funny"

        # act
        result = funnyString(s)

        # assert
        self.assertEqual(
            result, expected_output, "Differences [2, 21, 2] match reversed."
        )

    def test_bcxz_is_not_funny(self):
        # arrange
        s = "bcxz"
        expected_output = "Not Funny"

        # act
        result = funnyString(s)

        # assert
        self.assertEqual(
            result, expected_output, "Differences [1, 21, 2] do not match reversed."
        )

    def test_lmnop_is_funny(self):
        # arrange
        s = "lmnop"
        expected_output = "Funny"

        # act
        result = funnyString(s)

        # assert
        self.assertEqual(
            result, expected_output, "Differences are all 1s, which is a palindrome."
        )

    def test_identical_characters_are_funny(self):
        # arrange
        s = "zzzzz"
        expected_output = "Funny"

        # act
        result = funnyString(s)

        # assert
        self.assertEqual(result, expected_output, "Differences are all 0s.")

    def test_random_word_is_not_funny(self):
        # arrange
        s = "apple"
        expected_output = "Not Funny"

        # act
        result = funnyString(s)

        # assert
        self.assertEqual(
            result, expected_output, "Differences for 'apple' do not mirror."
        )
