#!/usr/bin/python3
"""Json Class object info"""


def class_to_json(obj):
    """Returns objects attributes

    Args:
        obj (object): python3 class object
    """
    s = obj.__dict__
    return s
