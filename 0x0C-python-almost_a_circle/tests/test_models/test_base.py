#!/usr/bin/python3
"""Simple unittest module"""
import unittest
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

    def test_char_id(self):
        """Test for a char id value"""
        self.assertRaises(TypeError, Base('a'), "unsupported operand type(s) for +: 'int' and 'str'")

    def test_list_id(self):
        """Test for a char id value"""
        self.assertRaises(TypeError, Base(['a']), "unsupported operand type(s) for +: 'int' and 'list'")

    def test_tuple_id(self):
        """Test for a char id value"""
        self.assertRaises(TypeError, Base(('a',)), "unsupported operand type(s) for +: 'int' and 'tuple'")

    def test_dict_id(self):
        """Test for a char id value"""
        self.assertRaises(TypeError, Base({'a': 23}), "unsupported operand type(s) for +: 'int' and 'str'")


if __name__ == "__main__":
    unittest.main()
