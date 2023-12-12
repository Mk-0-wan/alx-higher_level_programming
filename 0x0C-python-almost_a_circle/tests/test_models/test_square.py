#!/usr/bin/python3
"""Unittest for the square class"""
from models.square import Square
import unittest
import io
from unittest.mock import patch

class TestRectangle(unittest.TestCase):
    """Test Rectangle class"""

    def test_cls_doc(self):
        """Test class doc """
        self.assertFalse(len(Square.__doc__) == 0)

    def test_init(self):
        """Test for the initialized attributes"""
        s1 = Square(6)
        self.assertEqual(s1.size, 6)
        self.assertEqual(s1.width, 6)
        self.assertEqual(s1.height, 6)

    def test_disply(self):
        """Test for how to display"""

        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            s1 = Square(3)
            s1.display()
            self.assertEqual(mock_stdout.getvalue(),
                             '###\n###\n###\n')

    def test_update(self):
        """Test for the update function"""

        s1 = Square(5)

        with patch('sys.stdout', new_callable=io.StringIO) as mock_stdout:
            s1.update(10)
            print(s1)
            self.assertEqual(mock_stdout.getvalue(),
                             '[Square] (10) 0/0 - 5\n')
