#!/usr/bin/python3
"""Appending to a file"""


def append_write(filename="", text=""):
    """Appends text to the end of the file pointer

    Args:
        filename (str): file pointer to the file to append to
        text (str): data to append at the end of the file
    Return:
        returns the number of characters added
    """
    with open(filename, "a", encoding="utf-8") as fp:
        x = fp.write(text)
    return x
