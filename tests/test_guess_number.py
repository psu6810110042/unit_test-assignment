import unittest
from unittest import mock
import _6810110042.guess_number as guess_number


class GuessNumberTest(unittest.TestCase):
    @mock.patch("random.randint", return_value=15)
    def test_guess_int_should_return_mocked_value(self, mock_randint):
        start = 10
        stop = 20
        
        result = guess_number.guess_int(start, stop)
        
        self.assertEqual(result, 15)
        mock_randint.assert_called_once_with(start, stop)

    @mock.patch("random.uniform", return_value=12.5)
    def test_guess_float_should_return_mocked_value(self, mock_uniform):
        start = 10.0
        stop = 20.0
        
        result = guess_number.guess_float(start, stop)
        
        self.assertEqual(result, 12.5)
        mock_uniform.assert_called_once_with(start, stop)
