#!/usr/bin/python3
"""Writing to a file"""


def write_file(filename="", text=""):
    """Writing to a file and returns the number char written

   Args:
        filename (str):name of the file to write to
        text (str): input data to be written
    Return:
        number of chars written by the user
    """
    with open(filename, "w", encoding="utf-8") as fp:
        ln = fp.write(text)
    return ln
