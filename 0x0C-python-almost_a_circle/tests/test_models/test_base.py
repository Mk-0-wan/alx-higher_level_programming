#!/usr/bin/python3
"""Simple unittest module"""
import os
import sys
import json
import pep8
import unittest
from io import StringIO
from models.base import Base
from models.square import Square
from models.rectangle import Rectangle


class TestId(unittest.TestCase):
    """simple test unit for id"""

    def test_id(self):
        """Test if id is an integer"""
        Base._Base__nb_objects = 0
        b1 = Base()
        self.assertEqual(b1.id, int(1))

        a1 = Rectangle(34, 42)
        self.assertEqual(a1.id, int(2))

        c1 = Square(23, 23)
        self.assertEqual(c1.id, int(3))

        b1 = Base()
        self.assertEqual(b1.id, int(4))

        b1 = Base(32)
        self.assertEqual(b1.id, int(32))

        b1 = Base()
        self.assertEqual(b1.id, int(5))

        b2 = Base()
        b2._Base__nb_objects == 0
        self.assertEqual(b1.id, int(5))

    def test_documentation(self):
        """Testing for each method and class docstring"""
        self.assertTrue(hasattr(Base, "param_validator"))
        self.assertTrue(hasattr(Base, "create"))
        self.assertTrue(hasattr(Base, "_Base__nb_objects"))
        self.assertTrue(hasattr(Base, "to_json_string"))
        self.assertTrue(hasattr(Base, "from_json_string"))
        self.assertTrue(hasattr(Base, "save_to_file"))
        self.assertTrue(hasattr(Base, "load_from_file"))
        self.assertTrue(hasattr(Base, "save_to_file_csv"))
        self.assertTrue(hasattr(Base, "load_from_file_csv"))

    def test_pycodestyle_base(self):
        """Testing for pycodestyle implementation"""
        pycode = pep8.StyleGuide(quiet=True)
        py = pycode.check_files(['./models/base.py'])
        self.assertEqual(py.total_errors, 0, "error with pycodestyle")
        py = pycode.check_files(['./tests/test_models/test_base.py'])
        self.assertEqual(py.total_errors, 0,
                         'error with your pycodestyle implemetation')

    def test_for_empty_param(self):
        """Testing for empty params"""
        Rectangle.save_to_file([])
        with open('Rectangle.json', 'r') as empty_file:
            self.assertEqual([], json.load(empty_file))

        lst = Rectangle.to_json_string([])
        self.assertIsInstance(lst, str)

        string = Rectangle.from_json_string([])
        self.assertIsInstance(string, list)

    def test_for_None_param(self):
        """Testing for None arguments"""
        Rectangle.save_to_file(None)
        with open('Rectangle.json', 'r') as none_file:
            self.assertEqual([], json.load(none_file))

        lst = Rectangle.to_json_string(None)
        self.assertIsInstance(lst, str)

        string = Rectangle.from_json_string(None)
        self.assertIsInstance(string, list)

    def test_to_json_string(self):
        """Testing all the working possibilites"""
        json_list = Rectangle.to_json_string([{'id': 12}])
        self.assertIsInstance(json_list, str)

        json_list = Rectangle.to_json_string([{'id': 22}])
        self.assertIsInstance(json_list, str)

    def test_from_json_string(self):
        """Testing all the working possibilites"""
        json_list = json.dumps([{'id': 89}])
        json_list_1 = json.dumps([{'id': 33}])

        python_list = Rectangle.from_json_string(json_list)
        self.assertIsInstance(python_list, list)

        python_list_1 = Rectangle.from_json_string(json_list_1)
        self.assertIsInstance(python_list_1, list)

    def test_for_doctstring(self):
        """Testing for all the methods class and file doctstrings"""
        self.assertIsNotNone(Base.__doc__)
        self.assertIsNotNone(Base.param_validator.__doc__)
        self.assertIsNotNone(Base.create.__doc__)
        self.assertIsNotNone(Base.to_json_string.__doc__)
        self.assertIsNotNone(Base.from_json_string.__doc__)
        self.assertIsNotNone(Base.load_from_file.__doc__)
        self.assertIsNotNone(Base.save_to_file.__doc__)
        self.assertIsNotNone(Base.save_to_file_csv.__doc__)
        self.assertIsNotNone(Base.load_from_file_csv.__doc__)

    def test_to_save_file(self):
        """Test for all the file openning and writting json file"""
        # TODO: is the correct way Rectangle([1,12,3])
        list_of_rectangle = [
            {'x': 2, 'width': 10, 'id': 1, 'height': 7, 'y': 8},
            {'x': 3, 'width': 5, 'id': 20, 'height': 9, 'y': 1}
        ]

        Rectangle.save_to_file(list_of_rectangle)
        # check if the file is there
        self.assertTrue(os.path.isfile('Rectangle.json'))

        # check if the file content has data
        with open('Rectangle.json', 'r') as rect_file:
            rect_objects = sum(1 for _ in rect_file)
        self.assertGreater(rect_objects, 0)

        rect_list = Rectangle.load_from_file()
        for rect in rect_list:
            self.assertIsInstance(rect, Rectangle)

        list_of_square = [
            {'size': 9, 'x': 4, 'y': 3, 'id': 89},
            {'size': 20, 'x': 3, 'y': 4, 'id': 19}
        ]

        Square.save_to_file(list_of_square)
        self.assertTrue(os.path.isfile('Square.json'))

        # check if the file content has data
        with open('Square.json', 'r') as sq_file:
            sq_objects = sum(1 for _ in sq_file)
        self.assertGreater(sq_objects, 0)

        sq_list = Square.load_from_file()
        for sq in sq_list:
            self.assertIsInstance(sq, Square)

    def test_load_from_file(self):
        """Test for checking for all
        the saved file during loading the data inside"""
        r1 = Rectangle(10, 7, 2, 8)
        r2 = Rectangle(2, 4)
        list_rectangles_input = [r1, r2]

        Rectangle.save_to_file(list_rectangles_input)

        list_rectangles_output = Rectangle.load_from_file()

        for rect in list_rectangles_output:
            self.assertIsInstance(rect, Rectangle)

        s1 = Square(5)
        s2 = Square(7, 9, 1)
        list_squares_input = [s1, s2]

        Square.save_to_file(list_squares_input)

        list_squares_output = Square.load_from_file()

        for sq in list_squares_output:
            self.assertIsInstance(sq, Square)

    def test_create(self):
        """Test cases for the create class method"""
        Base._Base__nb_objects = 0
        r1 = Rectangle(3, 5, 1)
        r1_dictionary = r1.to_dictionary()
        r2 = Rectangle.create(**r1_dictionary)

        self.assertEqual(r1.__str__(), '[Rectangle] (1) 1/0 - 3/5')
        self.assertEqual(r2.__str__(), '[Rectangle] (1) 1/0 - 3/5')
        self.assertFalse(r1 is r2)
        self.assertFalse(r1 == r2)
        self.assertEqual(r1.id, r2.id)
        self.assertEqual(r1.area(), r2.area())
        self.assertEqual(r1.width, r2.width)

        s1 = Square(10, 2, 1)
        s1_dictionary = s1.to_dictionary()
        s3 = Square.create(**s1_dictionary)
        self.assertEqual(s1.__str__(), '[Square] (3) 2/1 - 10')
        self.assertEqual(s3.__str__(), '[Square] (3) 2/1 - 10')
        self.assertFalse(s1 is s3)
        self.assertFalse(s1 == s3)
        self.assertEqual(s1.id, s3.id)
        self.assertEqual(s1.size, s3.size)
        self.assertEqual(s1.area(), s3.area())

    def test_save_to_file_and_load_from_file_with_no_args_passed(self):
        """Testing for both no param passed when no param are passed"""

        rect_list = Rectangle.load_from_file()
        for rect in rect_list:
            self.assertIsInstance(rect, Rectangle)

        sq_list = Square.load_from_file()
        for sq in sq_list:
            self.assertIsInstance(sq, Square)

        try:
            os.remove("Rectangle.json")
        except Exception:
            pass
        rect_list = Rectangle.load_from_file()
        self.assertEqual(len(rect_list), 0)
        self.assertIsInstance(rect_list, list)

        try:
            os.remove("Square.json")
        except Exception:
            pass
        sq_list = Square.load_from_file()
        self.assertEqual(len(sq_list), 0)
        self.assertIsInstance(sq_list, list)

        Rectangle.save_to_file([Rectangle(1, 2)])
        self.assertTrue(os.path.isfile('Rectangle.json'))

        with open('Rectangle.json', 'r', encoding="utf-8") as rect_file:
            rect_objects = sum(1 for _ in rect_file)
        self.assertGreater(rect_objects, 0)

        Square.save_to_file([Square(1)])
        self.assertTrue(os.path.isfile('Square.json'))

        with open('Square.json', 'r', encoding="utf-8") as sq_file:
            sq_objects = sum(1 for _ in sq_file)
        self.assertGreater(sq_objects, 0)
