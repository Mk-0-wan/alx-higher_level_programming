#!/usr/bin/python3

def remove_char_at(str, int):
    """
    str: positional argument of type string
    int: positional argument of type integer
    will iterate over the str positional argument
    int holds the index of char to remove from the string
    return a copy of the str which is mutated
    """
    copy_str = ''
    # Check for the edges cases (beyond or below the string len)
    if 0 <= int < len(str):
        for i, char in enumerate(str):
            if i == int:
                continue
            copy_str += char
        return (copy_str)
    else:
        # if fails just return the original str
        return (str)
