#!/usr/bin/python3
"""isinstance or is it"""


def is_kind_of_class(obj, a_class) -> bool:
    """checks if an object is an instance of a_class
    or a subclass of a_class

    Args:
        obj (object): a python object of any type
        a_class (class): any class type for python
    Return:
        a bool if an object is both an instance of that
        class or a subclass of that class
    """
    if obj and a_class:
        return isinstance(obj, a_class) or issubclass(type(obj), a_class)
