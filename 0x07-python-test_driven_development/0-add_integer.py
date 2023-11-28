#!/usr/bin/python3
"""Adding function in python"""


def add_integer(a, b=98):
    """Simple python function that adds two
        int value together
    Args:
        a (int): can be any type but will be typecasted
        an int value
        b (int): second value to perform the sum on
    Return:
        sum of the two values passed in the param
    """

    if not isinstance(a, (float, int)):
        raise TypeError("a must be an integer") 
    elif not isinstance(b, (float, int)):
        raise TypeError("b must be an integer") 

    res = int(a) + int(b)

    return int(res)
