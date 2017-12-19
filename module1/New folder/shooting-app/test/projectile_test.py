import unittest

from shooting import Projectile, Position, Velocity


class ProjectileTest(unittest.TestCase):
    def test_projectile_is_created_with_initial_position(self):
        projectile = Projectile(Position(5, 25))

        self.assertTrue(isinstance(projectile, Projectile))

    def test_position_changes_when_projectile_is_shoot(self):
        initial_position = Position()
        projectile = Projectile(initial_position)
        velocity = Velocity(Position(), Position(3, 5))

        projectile.shoot(velocity)

        self.assertTrue(isinstance(projectile.position(), Position))
        self.assertNotEqual(initial_position, projectile.position())

    def test_projectile_shot_to_the_floor_should_remain_there(self):
        initial_position = Position(5, 10)
        projectile = Projectile(initial_position)
        # velocity = Velocity(Position(), Position(0, -1))
        velocity = Velocity.create_from_values(1, -90)

        projectile.shoot(velocity)

        self.assertEqual(Position(5, 0), projectile.position(), "(5, 0) is not %s" % str(projectile.position()))

    def test_projectile_shot_horizontally_follows_a_parabolic_path(self):
        projectile = Projectile(Position(2, 4))
        velocity = Velocity.create_from_values(5, 0)

        projectile.shoot(velocity)

        self.assertAlmostEqual(6.5, projectile.position().x(), delta=0.5)


    def test_flightPath_is_an_object_ofFlightPathType(self):
        projectile = Projectile(Position(2, 4))
        velocity = Velocity.create_from_values(5, 0)

        self.assertIsNotNone(projectile.shoot(velocity))


if __name__ == "__main__":
    unittest.main()
