#!/usr/bin/python3
"""
A python class that inherits from the list class
"""


class MyList(list):
    """inherits from the class list class"""
    def __init__(self):
        """Initializes the list class"""
        super().__init__()

    def print_sorted(self):
        """An extension of the list class that prints
        a sorted list of integers in ascending order

        Return:
            a sorted list from the smallest value to
            the largest in the list
        """
        s_list = super().copy()
        print(sorted(map(int, s_list)))
