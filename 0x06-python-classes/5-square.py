#!/usr/bin/python3
"""Implementation of some methods adding exceptions"""


class Square:
    """A simple python Square class while learning OPP

    Handling some exception errors for the instance variables

    Attributes:
        size (unknown): param that's going to allow us to make
        the square calculation.

    """
    def __init__(self, size=0):
        """Initializes the instances variables for Square class.

        Args:
            size (unknown): Param that takes in a value which is later
            on transformed into a private variable
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """Calculates the square value of a given value

        Return:
            The square value of a given arguments
        """
        return self.__size ** 2

    @property
    def size(self):
        """Getter function which will be used to retrive the private size value

        Return:
            The private attribute is returned
        """
        return self.__size

    @size.setter
    def size(self, value):
        """Sets a new value to the private value, it mutates the private value

        Args:
            value (int): the new value for the private size
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        else:
            self.__size = value

    def my_print(self):
        """Artistic print function from the square of size

        """
        x = self.__size
        if (x == 0):
            print()
        else:
            y = x**2
            i = 1
            for _ in range(y):
                print("#" * x)
