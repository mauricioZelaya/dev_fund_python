import unittest

class PositionTest(unittest.TestCase):
    def test_fail(self):
        self.assertEqual(1, 2, "1 is not 2")

    def test_pass(self):
        n = 5
        self.assertEqual(4, n)


if __name__ == "__main__":
    unittest.main()


