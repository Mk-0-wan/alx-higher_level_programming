#!/usr/bin/python3
"""Implementation of some methods adding exceptions and __str__"""


class Square:
    """A simple python Square class while learning OPP

    Handling some exception errors for the instance variables

    Attributes:
        size (unknown): param that's going to allow us to make
        the square calculation.

    """
    def __init__(self, size=0, position=(0, 0)):
        """Initializes the instances variables for Square class.

        Args:
            size (unknown): Param that takes in a value which is later
            on transformed into a private variable
            position (tuple): Param that takes in two int tuple objects
            which will later be used to determine the position of space placing
        """
        self.size = size
        self.position = position

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
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @property
    def position(self):
        """Public position function that gets the retrives the position values

        Return:
            Retrives the private position values
        """
        return self.__position

    @position.setter
    def position(self, value):
        """Public position setter function that allows us
        to mutate the value of position

        Args:
            value (tuple): will be used to update the position values
        """
        if (not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value) or len(value) != 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """Artistic print function from the square of size"""
        x = self.__size
        y = self.__position
        if (x == 0):
            print()
        else:
            for _ in range(y[1]):
                print()
            for _ in range(x):
                print(" " * y[0] + "#" * x)

    def __str__(self):
        """Print string values"""
        lst = []
        x = self.__size
        y = self.__position
        if (x == 0):
            return "\n"
        else:
            lst.append("\n" * (y[1]-1))
            for _ in range(x):
                lst.append(" " * y[0] + "#" * x)
        return "\n".join(lst)
