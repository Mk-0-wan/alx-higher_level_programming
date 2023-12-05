#!/usr/bin/python3
"""Square class that inherits from Rectangle"""
Rectangle = __import__("9-rectangle").Rectangle


class Square(Rectangle):
    """Simple Square class"""

    def __init__(self, size):
        """initialization"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """area method"""
        return super().area()

    def __str__(self):
        """printing the square root"""
        super().__str__()
        return "[{}] {}/{}".format(
                self.__class__.__name__, self.__size, self.__size)
