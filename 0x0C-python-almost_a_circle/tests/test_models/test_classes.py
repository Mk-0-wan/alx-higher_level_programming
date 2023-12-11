#!/usr/bin/python3
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

class TestId(unittest.TestCase):
    """simple test unit for id"""
    def test_width_and_height_normal(self):
        """Testing for the width alone"""
        r1 = Rectangle(12, 13)
        self.assertEqual(r1.width, 12)
        self.assertEqual(getattr(r1, "width"), 12)
        self.assertEqual(r1.height, 13)
        self.assertEqual(getattr(r1, "height"), 13)

        r1.width = 2
        r1.height = 3
        self.assertEqual(r1.width, 2)
        self.assertEqual(getattr(r1, "width"), 2)
        self.assertEqual(r1.height, 3)
        self.assertEqual(getattr(r1, "height"), 3)

        setattr(r1, "height", 32)
        setattr(r1, "width", 23),
        self.assertEqual(r1.width, 23)
        self.assertEqual(getattr(r1, "width"), 23)
        self.assertEqual(r1.height, 32)
        self.assertEqual(getattr(r1, "height"), 32)

    def test_width_and_height_chars(self):
        """Testing for character values"""

        # TypeError for both width  and height
        r2 = Rectangle("Hello", "Redouane")
        self.assertRaises(TypeError, r2.width, "width must be an integer")
        r2 = Rectangle(9, "Redouane")
        self.assertRaises(TypeError, r2.height, "height must be an integer")
        # TypeError for dict
        r2 = Rectangle({"Hello": 3}, "Redouane")
        self.assertRaises(TypeError, r2.width, "width must be an integer")
        r2 = Rectangle(9, {"Redouane": 90})
        self.assertRaises(TypeError, r2.height, "height must be an integer")
        # TypeError for list
        r2 = Rectangle(["Hello"], "Redouane")
        self.assertRaises(TypeError, r2.width, "width must be an integer")
        r2 = Rectangle(9, ["Redouane"])
        self.assertRaises(TypeError, r2.height, "height must be an integer")
        # TypeError for tuple
        r2 = Rectangle(("Hello",), "Redouane")
        self.assertRaises(TypeError, r2.width, "width must be an integer")
        r2 = Rectangle(9, ("Redouane",))
        self.assertRaises(TypeError, r2.height, "height must be an integer")
        # TypeError for float


        # ValueError for Width
        r2 = Rectangle(9.1, 0)
        self.assertRaises(ValueError, r2.width, "width must be an integer")
        r2 = Rectangle(0, 0)
        self.assertRaises(ValueError, r2.width, "width must be > 0")
        r2 = Rectangle(-9, 0)
        self.assertRaises(ValueError, r2.width, "width must be > 0")

        # ValueError for Height
        r2 = Rectangle(1, -8)
        self.assertRaises(ValueError, r2.height, "height must be > 0")
        r2 = Rectangle(1, -8)
        self.assertRaises(ValueError, r2.height, "height must be > 0")
        r2 = Rectangle(1, 2.1)
        self.assertRaises(ValueError, r2.height, "height must be an integer")


        # TypeError for X
        r2 = Rectangle(43, 21, 2.1, 0)
        self.assertRaises(TypeError, r2.x, "x must be an integer")
        r2 = Rectangle(43, 2, 'c', 2)
        self.assertRaises(TypeError, r2.x, "x must be an integer")

        # TypeError for Y
        r2 = Rectangle(43, 2, 2, 2.1)
        self.assertRaises(TypeError, r2.y, "y must be an integer")
        r2 = Rectangle(43, 2.1, 4, 'y')
        self.assertRaises(TypeError, r2.y, "y must be an integer")

        # ValueError for Y
        r2 = Rectangle(43, 2.1, 4, -2)
        self.assertRaises(ValueError, r2.y, "y must be >= 0")

        # ValueError for X
        r2 = Rectangle(43, 2.1, -4, 0)
        self.assertRaises(ValueError, r2.x, "x must be >= 0")

if __name__ == "__main__":
    unittest.main()
