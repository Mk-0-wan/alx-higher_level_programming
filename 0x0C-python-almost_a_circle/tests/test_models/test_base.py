#!/usr/bin/python3
"""Simple unittest module"""
import unittest
from models.base import Base

class TestId(unittest.TestCase):
    """simple test unit for id"""

    def test_id(self):
        """Test if id is an integer"""
        b1 = Base()
        self.assertEqual(b1.id, int(32))
        b1 = Base(32)
        self.assertEqual(b1.id, int(32))
    def test_char_id(self):
        """Test for a char id value"""
        b1 = Base()
        b1 = Base('a')
        self.assertRaises()

if __name__ == "__main__":
    unittest.main()
