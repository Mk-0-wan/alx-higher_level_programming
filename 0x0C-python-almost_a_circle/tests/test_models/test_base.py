#!/usr/bin/python3
"""Simple unittest module"""
import os
import sys
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
        self.assertEqual(py.total_errors, 0, 'error with your pycodestyle implemetation')
