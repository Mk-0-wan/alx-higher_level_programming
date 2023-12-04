#!/usr/bin/python3
BaseGeometry = __import__("7-base_geometry").BaseGeometry
"""simple Base Class"""


# no use of builtin commands
class Rectangle(BaseGeometry):
    """Simple geometry class that inherits BaseGeometry"""

    def __init__(self, width, height):
        """initializing instance variables
        Args:
            width (int): integer width side of the Rectangle
            height (int): integer height value of the Rectangle
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height
