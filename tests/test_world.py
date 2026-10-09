import unittest

from physics.body import Body
from physics.ball import Ball
from physics.world import PhysicsWorld


class TestPhysicsWorld(unittest.TestCase):

    def setUp(self):
        self.world = PhysicsWorld()

    def test_add_body(self):
        body = Body()
        self.world.add_body(body)

        self.assertIn(body, self.world.bodies)

    def test_reject_duplicate_body(self):
        body = Body()
        self.world.add_body(body)

        with self.assertRaises(ValueError):
            self.world.add_body(body)

    def test_reject_non_body(self):
        with self.assertRaises(TypeError):
            self.world.add_body("not a body")

    def test_remove_body(self):
        body = Body()
        self.world.add_body(body)
        self.world.remove_body(body)

        self.assertNotIn(body, self.world.bodies)

    def test_step_updates_all_bodies(self):
        body = Body(x=0, y=5, vx=2)
        ball = Ball(x=0, y=10, gravity=0, vx=1)

        self.world.add_body(body)
        self.world.add_body(ball)

        self.world.step(1)

        self.assertAlmostEqual(body.x, 2)
        self.assertAlmostEqual(ball.x, 1)
        self.assertAlmostEqual(self.world.time, 1)

    def test_invalid_dt(self):
        with self.assertRaises(ValueError):
            self.world.step(0)


if __name__ == "__main__":
    unittest.main()