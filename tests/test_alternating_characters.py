from _6810110042.alternating_characters import alternatingCharacters
import unittest


class AlternatingCharactersTest(unittest.TestCase):
    def test_all_As(self):
        # arrange
        s = "AAAA"
        expected_output = 3

        # act
        result = alternatingCharacters(s)

        # assert
        self.assertEqual(result, expected_output, "Needs 3 deletions to become 'A'.")

    def test_all_Bs(self):
        # arrange
        s = "BBBBB"
        expected_output = 4

        # act
        result = alternatingCharacters(s)

        # assert
        self.assertEqual(result, expected_output, "Needs 4 deletions to become 'B'.")

    def test_already_alternating(self):
        # arrange
        s = "ABABABAB"
        expected_output = 0

        # act
        result = alternatingCharacters(s)

        # assert
        self.assertEqual(
            result, expected_output, "No deletions needed, already alternating."
        )

    def test_mixed_chunks(self):
        # arrange
        s = "AAABBB"
        expected_output = 4

        # act
        result = alternatingCharacters(s)

        # assert
        self.assertEqual(
            result, expected_output, "Needs 2 'A's and 2 'B's deleted to become 'AB'."
        )

    def test_random_sequence(self):
        # arrange
        s = "AAABBBABAB"
        expected_output = 4

        # act
        result = alternatingCharacters(s)

        # assert
        self.assertEqual(
            result,
            expected_output,
            "Needs 2 'A's and 2 'B's deleted from the front chunks.",
        )
