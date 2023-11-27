#!/usr/bin/python3
"""Simple Introduction to Python Rectangle Class"""


class Rectangle:
    """A simple python class creating a Rectangle class with python"""

    def __init__(self, width=0, height=0):
        """Initializing all the instances attributes

        Args:
            width (int): value for the longer side of a rectangle
            height (int): value for the shorter side of the rectangle
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Getting the initial width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Overwrites the initial value of width to the new one give

        Args:
            value (int): an int value greater than 0 which will represent the new longer side of the rectangle

        Return:
            A private instance attribute width value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Getting the initial width value"""
        return self.__height

    @height.setter
    def height(self, value):
        """Overwrites the initial value of height to the new one give

        Args:
            value (int): an int value greater than 0 which will represent the new longer side of the rectangle

        Return:
            A private instance attribute width value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

my_rectangle = Rectangle(2, 4)
print(my_rectangle.__dict__)

my_rectangle.width = 10
my_rectangle.height = 3
print(my_rectangle.__dict__)
