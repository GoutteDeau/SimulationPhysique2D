
import unittest

from physics.body import Body
from physics.rectangle import Rectangle


class TestRectangle(unittest.TestCase):

    def test_rectangle_dimensions(self):
        rectangle = Rectangle(width=4, height=2)

        self.assertEqual(rectangle.width, 4)
        self.assertEqual(rectangle.height, 2)

    def test_rectangle_inherits_body(self):
        rectangle = Rectangle(x=3, y=5, vx=2)

        self.assertIsInstance(rectangle, Body)
        self.assertEqual(rectangle.x, 3)
        self.assertEqual(rectangle.y, 5)
        self.assertEqual(rectangle.vx, 2)

    def test_rectangle_moves(self):
        rectangle = Rectangle(x=0, y=0, vx=2, vy=1)

        rectangle.update(1)

        self.assertAlmostEqual(rectangle.x, 2)
        self.assertAlmostEqual(rectangle.y, 1)

    def test_invalid_dimensions(self):
        with self.assertRaises(ValueError):
            Rectangle(width=0)

        with self.assertRaises(ValueError):
            Rectangle(height=-1)


if __name__ == "__main__":
    unittest.main()