#!/usr/bin/python3
"""Printing a square in python"""


def print_square(size):
    """Printing a simple python square

    Args:
        size (int): size of the square to be printed

    Return:
        a printed square
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif not isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")

    for _ in range(size):
        print("#" * size)
