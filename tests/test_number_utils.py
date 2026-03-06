from _6810110042.number_utils import is_prime_list

import unittest


class PrimeListTest(unittest.TestCase):
    def test_give_1_2_3_5_is_not_prime(self):
        prime_list = [1, 2, 3, 5]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_all_valid_primes(self):
        prime_list = [2, 3, 5, 7, 11, 13]
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_all_composite_numbers(self):
        prime_list = [4, 6, 8, 9, 10]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_mixed_primes_and_composites(self):
        prime_list = [2, 3, 4, 5]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)

    def test_empty_list(self):
        prime_list = []
        is_prime = is_prime_list(prime_list)
        self.assertTrue(is_prime)

    def test_zero_and_negatives(self):
        prime_list = [0, -5, -7, 2]
        is_prime = is_prime_list(prime_list)
        self.assertFalse(is_prime)
