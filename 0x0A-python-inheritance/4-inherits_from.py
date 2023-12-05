#!/usr/bin/python3
"""indirect and direct inheritance"""


def inherits_from(obj, a_class):
    """checks if an object inherits direct or indirectly
    from a_class
    or a subclass of a_class

    Args:
        obj (object): a python object of any type
        a_class (class): any class type for python
    Return:
        a bool if an object is both an instance of that
        class or a subclass of that class
    """
    return issubclass(obj.__class__, a_class) and type(obj) is not a_class
