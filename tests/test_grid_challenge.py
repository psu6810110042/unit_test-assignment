import unittest
from _6810110042.grid_challenge import gridChallenge


class GridChallengeTest(unittest.TestCase):
    def test_standard_yes_example(self):
        # arrange
        grid = ["ebacd", "fghij", "olmkn", "trpqs", "xywuv"]
        expected_output = "YES"

        # act
        result = gridChallenge(grid)

        # assert
        self.assertEqual(
            result,
            expected_output,
            "After row sort, columns should be perfectly alphabetical.",
        )

    def test_standard_no_example(self):
        # arrange
        grid = ["mpxz", "abcd", "wlmf"]
        expected_output = "NO"

        # act
        result = gridChallenge(grid)

        # assert
        self.assertEqual(
            result, expected_output, "Columns fail the alphabetical check."
        )

    def test_already_sorted_grid(self):
        # arrange
        grid = ["abc", "def", "ghi"]
        expected_output = "YES"

        # act
        result = gridChallenge(grid)

        # assert
        self.assertEqual(
            result, expected_output, "Grid is already sorted, should return YES."
        )

    def test_single_character_grid(self):
        # arrange
        grid = ["a"]
        expected_output = "YES"

        # act
        result = gridChallenge(grid)

        # assert
        self.assertEqual(
            result, expected_output, "A 1x1 grid is technically always sorted."
        )

    def test_single_column_fails(self):
        # arrange
        grid = ["z", "x", "y"]
        expected_output = "NO"

        # act
        result = gridChallenge(grid)

        # assert
        self.assertEqual(
            result,
            expected_output,
            "Rows are 1 char (so already 'sorted'), but col is z -> x -> y (Fails).",
        )
