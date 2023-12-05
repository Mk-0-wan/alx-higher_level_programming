#!/usr/bin/python3
"""A student class"""


class Student:
    """A student class"""

    def __init__(self, first_name, last_name, age):
        """initialization of instance attributes
        Args:
            first_name (str): string format of students name
            last_name (str): string format of students name
        """
        self.first_name = first_name
        self.last_name = last_name

    def to_json(self):
        """A dictionary representation of the class attributes"""
        return self.__dict__
