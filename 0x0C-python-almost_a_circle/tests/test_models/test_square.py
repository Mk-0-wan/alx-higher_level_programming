#!/usr/bin/python3
"""Unittest for the square class"""
from models.square import Square
from models.base import Base
import unittest
from io import StringIO
import sys
import pep8


class TestRectangle(unittest.TestCase):
    """Test Rectangle class"""

    def test_cls_doc(self):
        """Test class doc """
        self.assertFalse(len(Square.__doc__) == 0)
        self.assertIsNotNone(Square.size.__doc__)
        self.assertIsNotNone(Square.update.__doc__)
        self.assertIsNotNone(Square.to_dictionary.__doc__)

    def test_init(self):
        """Test for the initialized attributes"""
        s1 = Square(6)
        self.assertEqual(s1.size, 6)
        self.assertEqual(s1.width, 6)
        self.assertEqual(s1.height, 6)

    def test_pycodestyle_base(self):
        """Testing for the pycodestlye_square file"""
        pycode = pep8.StyleGuide(quiet=True)
        py = pycode.check_files(['./models/square.py'])
        self.assertEqual(py.total_errors, 0, "error with pycodestyle")
        py = pycode.check_files(['./tests/test_models/test_square.py'])
        self.assertEqual(py.total_errors, 0,
                         'error with your pycodestyle implemetation')

    def test_for_id_params(self):
        """Testing for all the id passed in  rectangle class"""
        Base._Base__nb_objects = 1
        s1 = Square(10, 2)
        s2 = Square(6, 3, 4)
        s3 = Square(4, 4, 5)
        s3.id = "a"
        self.assertEqual(s1.id, 2)
        self.assertEqual(s2.id, 3)
        self.assertEqual(s3.id, 'a')

    def test_all_param(self):
        """Testing all the possible param passed"""
        with self.assertRaises(TypeError):
            Square('v')
        with self.assertRaises(ValueError):
            Square(-8)
        with self.assertRaises(ValueError):
            Square(size=3, x=-2)
        with self.assertRaises(TypeError):
            Square(size=5, y='k')
        with self.assertRaises(TypeError):
            Square(size=8, y=8, x='O')
        with self.assertRaises(ValueError):
            Square(0)

    def test_str_square(self):
        """Testing the string format of the class square"""
        Base._Base__nb_objects = 0
        s1 = Square(5)
        self.assertEqual(s1.__str__(), "[Square] (1) 0/0 - 5")
        s2 = Square(2, 2)
        self.assertEqual(s2.__str__(), "[Square] (2) 2/0 - 2")
        s3 = Square(3, 1, 3)
        self.assertEqual(s3.__str__(), "[Square] (3) 1/3 - 3")

    def test_area_square(self):
        """Testing for the square method"""
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)
        s2 = Square(2, 2)
        self.assertEqual(s2.area(), 4)
        s3 = Square(3, 1, 3)
        self.assertEqual(s3.area(), 9)

    def test_update_square(self):
        """Testing for the update square class method"""
        Base._Base__nb_objects = 0
        s1 = Square(5)
        s1.update(10)
        self.assertEqual(str(s1), "[Square] (10) 0/0 - 5")
        s1.update(1, 2)
        self.assertEqual(str(s1), "[Square] (1) 0/0 - 2")
        s1.update(1, 2, 3)
        self.assertEqual(str(s1), "[Square] (1) 3/0 - 2")
        s1.update(1, 2, 3, 4)
        self.assertEqual(str(s1), "[Square] (1) 3/4 - 2")
        s1.update(size=7, y=1, x=12)
        self.assertEqual(str(s1), "[Square] (1) 12/1 - 7")
        s1.update(size=7, id=89, y=1)
        self.assertEqual(str(s1), "[Square] (89) 12/1 - 7")

    def test_display_square(self):
        """Testing the display square class"""
        std_post = sys.stdout

        sys.stdout = std_pull = StringIO()
        r1 = Square(3)
        r1.display()
        captured = std_pull.getvalue()

        sys.stdout = std_post  # return to the original post
        self.assertEqual(captured,
                         "###\n###\n###\n")

        sys.stdout = std_pull = StringIO()
        r1 = Square(2, 2)
        r1.display()
        captured = std_pull.getvalue()

        sys.stdout = std_post  # once you are done again clean stdout
        self.assertEqual(captured,
                         "  ##\n  ##\n")

    def test_to_dictionary_square(self):
        """Testing for the dictionary square class method"""
        Base._Base__nb_objects = 0
        s1 = Square(2, 2, 2, 2)
        s1_dictionary = s1.to_dictionary()
        self.assertDictEqual(s1_dictionary,
                             {'x': 2, 'y': 2, 'size': 2, 'id': 2})
        s1.update(size=10, x=2, y=1)
        s1_dictionary = s1.to_dictionary()
        self.assertDictEqual(s1_dictionary,
                             {'id': 2, 'x': 2, 'y': 1, 'size': 10})
