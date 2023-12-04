#!/usr/bin/python3
BaseGeometry = __import__("7-base_geometry").BaseGeometry
"""simple Base Class"""


# no use of builtin commands
class Rectangle(BaseGeometry):
    """Simple geometry class that inherits BaseGeometry"""

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
