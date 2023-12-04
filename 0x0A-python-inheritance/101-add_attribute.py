#!/usr/bin/python3
"""
A python function that adds new attribute to a class
And all of this is done by modifying the class dict

"""


def add_attribute(obj, key, new_val) -> object:
    """Adding new attribute to a class

    Args:
        obj (class): an instance of a new class
        key (str): a string data type which holds
        the new attribute to be added
        new_val (any): any type of data can be
        passed as the new attribute value
    Return:
        returns a new instance of the class obj
        with new initialized attributes
    """
    if hasattr(obj, "__dict__"):
        obj.__dict__[key] = new_val
    else:
        raise TypeError("can't add new attribute")
