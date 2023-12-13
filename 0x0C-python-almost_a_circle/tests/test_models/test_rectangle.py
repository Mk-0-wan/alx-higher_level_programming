#!/usr/bin/python3
"""Simple unittest module"""
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestId(unittest.TestCase):
    """simple test unit for id"""
    def test_width_and_height_normal(self):
        """Simple unittest for the tasks"""
        # TypeError for both width and height
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle("Hello", 5)

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, "Redouane")

        # TypeError for dict
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle({"Hello": 3}, "Redouane")

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, {"Redouane": 90})

        # TypeError for list
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(["Hello"], "Redouane")

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, ["Redouane"])

        # TypeError for tuple
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(("Hello",), "Redouane")

        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(9, ("Redouane",))

        # TypeError for float
        with self.assertRaisesRegex(TypeError, "width must be an integer"):
            Rectangle(9.1, 0)

        # ValueError for Width
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(0, 0)

        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Rectangle(-9, 0)

        # ValueError for Height
        with self.assertRaisesRegex(ValueError, "height must be > 0"):
            Rectangle(1, -8)
        with self.assertRaisesRegex(TypeError, "height must be an integer"):
            Rectangle(1, 2.1)

        # TypeError for X
        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(43, 21, 2.1, 0)

        with self.assertRaisesRegex(TypeError, "x must be an integer"):
            Rectangle(43, 2, 'c', 2)

        # TypeError for Y
        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(43, 2, 2, 2.1)

        with self.assertRaisesRegex(TypeError, "y must be an integer"):
            Rectangle(43, 2, 4, 'y')

        # ValueError for Y
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Rectangle(43, 2, 4, -2)

        # ValueError for X
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Rectangle(43, 2, -4, 0)
