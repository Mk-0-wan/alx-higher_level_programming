#!/usr/bin/python3
"""Simple unittest module"""
import unittest


class TestId(unittest.TestCase):
    """simple test unit for id"""

    def test_id(self):
        """Test if id is an integer"""
        x_int = int(32)
        self.assertEqual(x_int, int(12))

if __name__ == "__main__":
    unittest.main()
