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
        if attrs is None:
            return self.__dict__
        if not isinstance(attrs, list):
            return self.__dict__
        if not (isinstance(attrs[i], str) for i in attrs):
            return self.__dict__
        return ({key: value
                 for key, value in self.__dict__.items() if key in attrs})

    def relaod_from_json(self, json):
        """Adding a json format dictionary to the class attributes
        Args:
            json: json formatted dict values
        """
        self.first_name = json["first_name"]
        self.last_name = json["last_name"]
        self.age = json["age"]
