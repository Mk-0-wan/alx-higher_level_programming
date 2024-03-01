#!/usr/bin/python3
"""Simple implementation of the Bubble sort algorithm"""


def find_peak(list_of_integers):
    """Finds the peak in a list of integers"""
    if (len(list_of_integers) == 0):
        return
    # first we need a max value
    max_val = max(list_of_integers)
    # loop over each of the element comparing each one of them to each other
    i = 0
    # 1 ,2 ,4, 6  == len == 3 - 2 = 1 loop has two turn to make
    while (i < (len(list_of_integers) - 2)):
        if (list_of_integers[i] > list_of_integers[i + 1]):
            if (list_of_integers[i] > max_val):
                max_val = list_of_integers[i]
        else:
            if (list_of_integers[i + 1] > max_val):
                max_val = list_of_integers[i + 1]
        i += 1

    return max_val
