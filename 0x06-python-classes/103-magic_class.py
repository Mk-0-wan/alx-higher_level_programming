#!/usr/bin/python3
"""Simple Magic Calculatation"""
import math


class MagicClass:
    """Magic class bytecode"""
    def __init__(self, radius=None):
        """initializes the variables instances"""
        self._MagicClass__radius = 0
        if type(radius) is not int and type(radius) is not float:
            raise TypeError("radius must be a number")
        self._MagicClass__radius = radius

    def area(self):
        """calculates the area"""
        return self._MagicClass__radius ** 2 * math.pi

    def circumference(self):
        """calculates the circumference"""
        return 2 * math.pi * self._MagicClass__radius
