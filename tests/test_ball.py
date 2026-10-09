import unittest

from physics.body import Body
from physics.ball import Ball


class TestPhysics(unittest.TestCase):

    def test_ball_inherits_body(self):
        ball = Ball(x=0, y=10, gravity=0)
        self.assertIsInstance(ball, Body)

    def test_constant_velocity(self):
        ball = Ball(x=0, y=10, vx=2, gravity=0)
        ball.update(1)

        self.assertAlmostEqual(ball.x, 2)
        self.assertAlmostEqual(ball.y, 10)

    def test_gravity(self):
        ball = Ball(x=0, y=10)
        ball.update(1)

        self.assertAlmostEqual(ball.y, 5.095)
        self.assertAlmostEqual(ball.vy, -9.81)

    def test_invalid_dt(self):
        ball = Ball()

        with self.assertRaises(ValueError):
            ball.update(0)


if __name__ == "__main__":
    unittest.main()