#!/usr/bin/python3
"""Simple Introduction to Python Rectangle Class"""


class Rectangle:
    """A simple python class creating a Rectangle class with python

    Args:
        no_of_instances (int): Global public class variable which will
        keep the record of how many child instances were created and
        deleted.
    """
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initializing all the instances attributes

        Args:
            width (int): value for the longer side of a rectangle
            height (int): value for the shorter side of the rectangle
        """
        self.width = width
        type(self).number_of_instances += 1
        self.height = height

    @property
    def width(self):
        """Getting the initial width value"""
        return self.__width

    @width.setter
    def width(self, value):
        """Overwrites the initial value of width to the new one give

        Args:
            value (int): an int value greater than 0
                which will represent the new longer side of the rectangle

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
            value (int): an int value greater than 0
                which will represent the new longer side of the rectangle

        Return:
            A private instance attribute width value
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates the area of a rectangle

        Return:
            Area of the rectangle
        """
        return self.__width * self.__height

    def perimeter(self):
        """Calculates the parameter of a rectangle instance

        Return:
            Perimeter of the rectangle
        """
        if self.__height == 0 or self.width == 0:
            return 0
        return (self.__width + self.__height) * 2

    def __str__(self):
        """Returning the string format of both the perimeter and """
        lst = []
        if self.__width == 0 or self.__height == 0:
            return ""
        else:
            for _ in range(self.__height):
                lst.append("#" * self.__width)
        return "\n".join(lst)

    def __repr__(self):
        """Returns a string representation of the object as it is"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """Just deletes all the instances created"""
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
