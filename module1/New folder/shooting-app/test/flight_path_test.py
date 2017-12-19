import unittest

from shooting import Projectile, Position, Velocity, FlightPath

class FlihtPathTest(unittest.TestCase):

    def test_if_time_is_zero_postion_is_the_start_position(self):
        initial_position = Position()
        projectile = Projectile(initial_position)
        velocity = Velocity(initial_position, initial_position)
        flight_path=projectile.shoot(velocity)
        position_flight_path = flight_path.calculate_position(0)
       # time = projectile.(velocity)
        self.assertTrue(isinstance(position_flight_path, Position))

    def test_if_time_is_not_zero_when_postion_is_not_the_same_that_start_position(self):
        position = Position()
        projectile = Projectile()
        velocity = Velocity()
        flight_path = projectile.shoot(velocity)
        position_flight_path = flight_path.calculate_position(0)

        self.assertTrue(isinstance(position_flight_path, Position))


if __name__ == "__main__":
    unittest.main()
