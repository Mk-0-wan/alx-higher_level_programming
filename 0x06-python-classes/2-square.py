#!/usr/bin/python3
"""Implementation of some methods adding exceptions"""


class Square:
    """A simple python Square class while learning OPP

    Handling some exception errors for the instance variables

    Attributes:
        size (unknown): param that's going to allow us to make
        the square calculation.

    """
    def __init__(self, size=None):
        """Initializes the instances variables for Square class.

        Args:
            size (unknown): Param that takes in a value which is later
            on transformed into a private variable
        """
        if isinstance(size, int):
            self.__size = size
        else:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
