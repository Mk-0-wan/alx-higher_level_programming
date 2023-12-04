#!/usr/bin/python3
"""Instance checking"""


def is_same_class(obj, a_class) -> bool:
    """Shows the kind of relation each instance has with
    a specific type of class there is

    Args:
        obj (object): any type of python object
        a_class (class): any type of python class

    Return:
        a bool indicating if it's false or true
    """
    if obj is None or a_class is None:
        return
    return isinstance(obj, a_class) or issubclass(type(obj), a_class)
