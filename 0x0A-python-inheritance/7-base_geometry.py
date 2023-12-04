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
        if name is None or value is None:
            return
        elif not isinstance(value, int):
            raise TypeError("{:s} must be an integer".format(name))
        elif value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
