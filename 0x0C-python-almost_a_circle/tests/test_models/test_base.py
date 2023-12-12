#!/usr/bin/python3
"""Simple unittest module"""
import unittest
import pep8
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square

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

    def test_pep8_base(self):
        """Test that the base module conforms to PEP8."""
        style = pep8.StyleGuide()
        result = style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style errors (and warnings).")

    def test_cls_doc(self):
        """Test class doc """

        self.assertFalse(len(Base.__doc__) == 0)

    def test_init(self):
        """Test __init__"""

        b1 = Base()
        b2 = Base()
        b3 = Base()
        b4 = Base(12)
        b5 = Base()
        self.assertEqual(b1.id, 1)
        self.assertEqual(b2.id, 2)
        self.assertEqual(b3.id, 3)
        self.assertEqual(b4.id, 12)
        self.assertEqual(b5.id, 4)
