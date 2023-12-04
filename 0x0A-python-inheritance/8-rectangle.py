#!/usr/bin/python3
"""simple Base Class"""


class BaseGeometry:
    """An empty Base class"""

    def __init__(self):
        """initializes the class instances attribute"""
        pass

    def area(self):
        """simple area function that raises an exception error
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates if a value is an integer

        Args:
            name (str): a string value for the method validator
            value (int): integer value for the validator
        Return:
            raises some exception errors
        """
        if type(value) is not int:
            raise TypeError("{:s} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))


class Rectangle(BaseGeometry):
    """Simple geometry class that inherits from BaseGeometry"""

    def __init__(self, width, height):
        """initializing instance variables
        Args:
            width (int): integer for the longest side of the Rectangle
            height (int): integer value for the shortest side
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
