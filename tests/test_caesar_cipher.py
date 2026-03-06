from _6810110042.ceasar_cipher import caesarCipher
import unittest


class CaesarCipherTest(unittest.TestCase):
    def test_standard_shift_with_symbols(self):
        # arrange
        s = "middle-Outz"
        k = 2
        expected_output = "okffng-Qwvb"

        # act
        result = caesarCipher(s, k)

        # assert
        self.assertEqual(
            result,
            expected_output,
            "Should shift letters by 2, preserve case, and ignore hyphens.",
        )

    def test_wrap_around_alphabet(self):
        # arrange
        s = "xyz"
        k = 5
        expected_output = "cde"

        # act
        result = caesarCipher(s, k)

        # assert
        self.assertEqual(
            result,
            expected_output,
            "Should wrap around 'z' back to the start of the alphabet.",
        )

    def test_large_shift_number(self):
        # arrange
        s = "Hello-World!"
        k = 100
        expected_output = "Dahhk-Sknhz!" 

        # act
        result = caesarCipher(s, k)

        # assert
        self.assertEqual(
            result,
            expected_output,
            "Should correctly reduce the large shift using modulo 26.",
        )

    def test_only_symbols_and_numbers(self):
        # arrange
        s = "12345!@#$%"
        k = 15
        expected_output = "12345!@#$%"

        # act
        result = caesarCipher(s, k)

        # assert
        self.assertEqual(
            result,
            expected_output,
            "Should return the exact same string since there are no letters.",
        )

    def test_zero_shift(self):
        # arrange
        s = "NoShift"
        k = 0
        expected_output = "NoShift"

        # act
        result = caesarCipher(s, k)

        # assert
        self.assertEqual(
            result,
            expected_output,
            "Should return the original string when shifted by 0.",
        )
