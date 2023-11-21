#!/usr/bin/python3
"""Implementation of some methods"""


class Square:
    """A simple python Square class while learning OPP

    Simple square class that does nothing at the moment.

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
        self.__size = size
