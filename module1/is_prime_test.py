import unittest
from is_prime import is_prime


class PrimeTest(unittest.TestCase):

    # def setup(self):
    #     self.x = 5

    def test_5_is_prime(self):
        self.assertTrue(is_prime(5), "TRUE")

    def test_9_is_not_prime(self):
        self.assertFalse(is_prime(9), "TRUE")

    def test_4_is_not_prime(self):
        self.assertFalse(is_prime(4), "TRUE")

    def test_1_is_not_prime(self):
        self.assertFalse(is_prime(1), "TRUE")


if __name__ == '__main__':
    unittest.main()

