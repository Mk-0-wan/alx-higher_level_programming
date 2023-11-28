#!/usr/bin/python3
"""Text manipulation with python"""


def text_indentation(text):
    """A function which replaces all the . ? and : with newlines

    Args:
        text (string): a bunch of text
    Return:
        text where all the special chars are replaced with newlines
    """

    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_string = ""
    special_char = ['.', '?', ':']

    for char in text:
        new_string += char
        if char in special_char:
            new_string += "\n\n"

    lines = new_string.split('\n')
    cleaned_lines = [line.lstrip() for line in lines]
    result = '\n'.join(cleaned_lines)
    print(result, end='')
