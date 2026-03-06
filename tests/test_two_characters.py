import unittest
from _6810110042.two_characters import alternate


class AlternateTest(unittest.TestCase):

    def test_standard_example(self):
        # arrange
        s = "beabeefeab"
        expected_output = 5

        # act
        result = alternate(s)

        # assert
        self.assertEqual(
            result,
            expected_output,
            "The longest alternating string should be 'babab' with length 5.",
        )

    def test_already_alternating(self):
        # arrange
        s = "xyxyxy"
        expected_output = 6

        # act
        result = alternate(s)

        # assert
        self.assertEqual(
            result,
            expected_output,
            "String is already perfect, should return its full length.",
        )

    def test_all_identical_characters(self):
        # arrange
        s = "aaaaa"
        expected_output = 0

        # act
        result = alternate(s)

        # assert
        self.assertEqual(
            result,
            expected_output,
            "Cannot form a two-character alternating string, should be 0.",
        )

    def test_no_valid_combinations(self):
        # arrange
        s = "abccba"
        expected_output = 0

        # act
        result = alternate(s)

        # assert
        self.assertEqual(
            result,
            expected_output,
            "No valid alternating pairs exist, should return 0.",
        )

    def test_single_character(self):
        # arrange
        s = "a"
        expected_output = 0

        # act
        result = alternate(s)

        # assert
        self.assertEqual(
            result, expected_output, "Less than two characters, cannot alternate."
        )
