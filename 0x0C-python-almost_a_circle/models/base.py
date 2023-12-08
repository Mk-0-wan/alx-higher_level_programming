#!/usr/bin/python3
"""Base class for all the other classes"""


class Base():
    """Simple entry point for a whole project almost a circle
    Args:
        __nb_objects (int): private class variable
    """
    __nb_objects = 0

    def __init__(self, id=None) -> None:
        """Initializes instances variables
        Args:
            id (none): will be used to later on to update the private
            class variable
        """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
