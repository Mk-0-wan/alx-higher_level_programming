#!/usr/bin/python3
"""Unittest for max_integer([..])
"""
import unittest
max_integer = __import__('6-max_integer').max_integer

class TestMaxInteger(unittest.TestCase):
    """Simple unittest class for testing task 6"""

    def test_empty_max_integer(self):
        """Test for the case of empty max_integer list"""
        self.assertEqual(max_integer([]), None)

    def test_pos_max_integer(self):
        """Testing for the case where all integers are positive"""
        tl = [1,3,5,7,11,23,4]
        self.assertEqual(max_integer(tl), 23)

    def test_neg_max_integer(self):
        """Testing for the case where negative integers are present"""
        tl = [1,2,-3,5,-3,-1]
        self.assertEqual(max_integer(tl), 5)
