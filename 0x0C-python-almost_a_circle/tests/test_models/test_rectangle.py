#!/usr/bin/python3
"""Simple unittest module"""
import unittest
import pep8
import sys
from io import StringIO
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square


class TestRectangle(unittest.TestCase):
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

    def test_to_json_string(self):
        """Testing all the working possibilites"""
        lst = [
            {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8},
            {'x': 3, 'width': 5, 'id': 20, 'height': 9, 'y': 1}
        ]
        json_list = Rectangle.to_json_string(lst)
        python_list = Rectangle.from_json_string(json_list)
        self.assertIsInstance(lst, list)
        self.assertIsInstance(json_list, str)
        self.assertIsInstance(python_list, list)

    def test_for_doctstring(self):
        """Testing for all the function docstring"""
        self.assertIsNotNone(Rectangle.__doc__)
        self.assertIsNotNone(Rectangle.width.__doc__)
        self.assertIsNotNone(Rectangle.height.__doc__)
        self.assertIsNotNone(Rectangle.x.__doc__)
        self.assertIsNotNone(Rectangle.y.__doc__)
        self.assertIsNotNone(Rectangle.area.__doc__)
        self.assertIsNotNone(Rectangle.display.__doc__)
        self.assertIsNotNone(Rectangle.__str__.__doc__)
        self.assertIsNotNone(Rectangle.update.__doc__)
        self.assertIsNotNone(Rectangle.to_dictionary.__doc__)

    def test_pycodestyle_rectangle(self):
        """Testing for all the pycodestyle errors inside the rectangle file"""
        pycode = pep8.StyleGuide(quiet=True)
        py = pycode.check_files(['./models/rectangle.py'])
        self.assertEqual(py.total_errors, 0, "error with pycodestyle")
        py = pycode.check_files(['./tests/test_models/test_rectangle.py'])
        self.assertEqual(py.total_errors, 0,
                         'error with your pycodestyle implemetation')

    def test_for_id_params(self):
        """Testing for all the id passed in  rectangle class"""
        Base._Base__nb_objects = 1
        r1 = Rectangle(10, 2)
        r2 = Rectangle(1, 6, 3, 4, 5)
        r3 = Rectangle(2, 4, 4, 5, 3)
        r3.id = "a"
        self.assertEqual(r1.id, 2)
        self.assertEqual(r2.id, 5)
        self.assertEqual(r3.id, 'a')

    def test_for_area(self):
        """Testing for the class area method"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(3, 2)
        r2 = Rectangle(2, 10)
        r3 = Rectangle(8, 7, 0, 0, 12)

        self.assertEqual(r1.area(), 6)
        self.assertEqual(r2.area(), 20)
        self.assertEqual(r3.area(), 56)

    def test_for_display(self):
        """Testing for the display class method"""
        # quite tricky at first you will need a varibale to store output
        # direct the var data to the output using sys
        # then compare the two if they are valid
        # store whatever was there before
        std_post = sys.stdout

        sys.stdout = std_pull = StringIO()
        r1 = Rectangle(3, 2, 1, 0)
        r1.display()
        captured = std_pull.getvalue()

        sys.stdout = std_post  # return to the original post
        self.assertEqual(captured,
                         " ###\n ###\n")

        sys.stdout = std_pull = StringIO()
        r1 = Rectangle(2, 3, 2, 2)
        r1.display()
        captured = std_pull.getvalue()

        sys.stdout = std_post  # once you are done again clean stdout
        self.assertEqual(captured,
                         "\n\n  ##\n  ##\n  ##\n")

    def test_update(self):
        """Testing the display  Rectangle class method"""
        r1 = Rectangle(10, 10, 10, 10)

        r1.update(89)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 10/10")
        r1.update(89, 2)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/10")
        r1.update(89, 2, 3)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 10/10 - 2/3")
        r1.update(89, 2, 3, 4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/10 - 2/3")
        r1.update(89, 2, 3, 4, 5)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 4/5 - 2/3")
        r1.update(width=12, height=22, x=2, y=4)
        self.assertEqual(r1.__str__(), "[Rectangle] (89) 2/4 - 12/22")

        with self.assertRaises(TypeError, msg="x must be an integer"):
            r1.update(x='fuzz', y=2, width=2, height=8)

        with self.assertRaises(ValueError, msg="x must be >= 0"):
            r1.update(x=-2, y=2, width=9, height=12)

        with self.assertRaises(TypeError, msg="width must be an integer"):
            r1.update(x=2, y=2, width="fuzz", height=12)

        with self.assertRaises(ValueError, msg="height must be > 0"):
            r1.update(x=2, y=2, width=9, height=-3)

    def test_to_dictionary(self):
        """Testing for to dictionary Rectangle class method"""
        Base._Base__nb_objects = 0  # all the value are starting at zero
        r1 = Rectangle(10, 2, 1, 9)
        r1_dict = r1.to_dictionary()

        self.assertDictEqual(r1_dict,
                             {
                                 'x': 1,
                                 'y': 9,
                                 'id': 1,
                                 'height': 2,
                                 'width': 10
                                 })

        Base._Base__nb_objects = 0  # all the value are starting at zero
        r2 = Rectangle(1, 1)
        r2_dict = r2.to_dictionary()

        self.assertDictEqual(r2_dict,
                             {
                                 'x': 0,
                                 'y': 0,
                                 'id': 1,
                                 'width': 1,
                                 'height': 1
                                 })
