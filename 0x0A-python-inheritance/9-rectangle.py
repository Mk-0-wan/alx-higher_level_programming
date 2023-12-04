#!/usr/bin/python3
"""simple task implementation"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Simple geometry class that inherits BaseGeometry"""

    def __init__(self, width, height):
        """initializing instance variables
        Args:
            width (int): integer width side of the Rectangle
            height (int): integer height value of the Rectangle
        """
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """returns the area of a Rectangle"""
        return self.__width * self.__height

    def __str__(self):
        """in built string function"""
        return "[{}] {}/{}".format(
                self.__class__.__name__, self.__width, self.__height)
