import unittest
from shooting import Position

class PositionTest(unittest.TestCase):
    def test_position_can_be_created_with_no_params(self):
        position = Position()
        self.assertIsNotNone(position)

    def test_position_with_no_params_corresponds_to_origin(self):
        position = Position()
        self.assertEqual(0, position.x())
        self.assertEqual(0, position.y())

    def test_position_can_be_created_with_x_and_y_params(self):
        position = Position(2,3)
        self.assertEqual(2, position.x())
        self.assertEqual(3, position.y())

    def test_distance_to_same_position_is_zero(self):
        position = Position(1, 3)
        self.assertEqual(0, position.distance_to(position))

    def test_distance_is_greater_than_zero_if_positions_are_diff(self):
        first_position = Position()
        second_position = Position(1, 1)
        self.assertTrue(first_position.distance_to(second_position) > 0)

    def test_positions_with_same_coordinates_are_equals(self):
        first_pos = Position(1, 2)
        second_pos = Position(1, 2)

        self.assertEqual(first_pos, second_pos)

    def test_positions_with_different_coordinates_are_not_equals(self):
        first_pos = Position(1, 2)
        second_pos = Position(1, 3)

        self.assertNotEqual(first_pos, second_pos)


if __name__ == "__main__":
    unittest.main()


