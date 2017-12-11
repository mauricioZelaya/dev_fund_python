import unittest
import math
from shooting import Position
from shooting import Velocity


class VelocityTest(unittest.TestCase):

    def test_create_velocity_with_two_positions(self):
        start_position = Position()
        end_position = Position(4, 3)

        velocity = Velocity()

        self.assertIsNotNone(velocity)
        self.assertIsNotNone(velocity.create_from_positions(start_position, end_position))

    def test_magnitude_is_zero_if_start_and_end_positions_are_the_same(self):
        position = Position(1,1)
        velocity = Velocity(position, position)

        self.assertEqual(0, velocity.magnitude())

    def test_magnitude_of_velocity_is_given_by_pythagoras_theorem(self):
        start_position = Position()
        end_position = Position(4, 3)

        velocity = Velocity(start_position, end_position)

        self.assertEqual(5, velocity.magnitude())

    def test_angle_of_velocoty_is_45_if_x_and_y_of_end_position_are_the_same(self):
        start_position = Position()
        end_position = Position(2, 2)

        velocity = Velocity(start_position, end_position)

        self.assertEqual(45, velocity.angle())

    def test_angle_of_velpcity_is_determined_by_the_arctangent(self):
        start_position = Position()
        end_position = Position(3, 4)
        angle = math.degrees(math.atan(4/3))

        velocity = Velocity(start_position, end_position)

        self.assertEqual(angle, velocity.angle())


    def test_velocity_can_be_created_with_magnitude_and_angle(self):
        velocity = Velocity(5, 45)
        self.assertEqual(45, velocity.angle())
        self.assertEqual(5, velocity.magnitude())

if __name__ == "__main__":
    unittest.main()
