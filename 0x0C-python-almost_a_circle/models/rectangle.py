#!/usr/bin/python3
"""A rectangle class that inherits from Base class"""
from models.base import Base


class Rectangle(Base):
    """docstring for Rectangle"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes all the instance attributes
        Args:
            width (int): an integer value holding the with of the Rectangle
            height (int): height of the rectangle
            x (int): just an x value
            y (int): just a y int value
            id (int): id value
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y


    @property
    def width(self) -> int:
        """Simple width getter"""
        return self.__width

    @property
    def height(self) -> int:
        """Simple height getter"""
        return self.__height

    @property
    def x(self) -> int:
        """Simple x getter"""
        return self.__x

    @property
    def y(self) -> int:
        """Simple y getter"""
        return self.__y

    @width.setter
    def width(self, value):
        """Simple width setter
        Args:
            value (int): new value to assign to the instance attribute
        Return:
            returns a new mangled width for the instance variable
        """
        self.__width = value
        return self.__width

    @height.setter
    def height(self, value):
        """Simple width setter
        Args:
            value (int): new value to assign to the instance attribute
        Return:
            returns a new mangled width for the instance variable
        """
        self.__height = value
        return self.__height

    @x.setter
    def x(self, value):
        """Simple width setter
        Args:
            value (int): new value to assign to the instance attribute
        Return:
            returns a new mangled width for the instance variable
        """
        self.__x = value
        return self.__x

    @y.setter
    def y(self, value):
        """Simple width setter
        Args:
            value (int): new value to assign to the instance attribute
        Return:
            returns a new mangled width for the instance variable
        """
        self.__y = value
        return self.__y

