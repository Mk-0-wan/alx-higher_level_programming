#!/usr/bin/python3
"""A student class"""


class Student:
    """A student class"""

    def __init__(self, first_name, last_name, age):
        """initialization of instance attributes
        Args:
            first_name (str): string format of students name
            last_name (str): string format of students name
            age (int): students age
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """A dictionary representation of the class attributes"""
        if attrs is not None and all(isinstance(attrs, list)
                                     or isinstance(attrs[i], str)
                                     for i in attrs):
            return ({key: value
                     for key, value in self.__dict__.items() if key in attrs})

        return self.__dict__
