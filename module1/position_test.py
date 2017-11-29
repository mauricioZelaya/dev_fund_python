import unittest

class PositionTest(unittest.TestCase):
    def test_fail(self):
        self.assertEqual(1, 2, "1 is not 2")
        self.assertTrue(False)

if __name__ == "__main__":
    unittest.main()


