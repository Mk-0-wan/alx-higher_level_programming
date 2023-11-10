#!/usr/bin/python3
def update_dictionary(a_dictionary, key, value):
    # find a key in the dict
    lc = list(a_dictionary.keys())

    key_found = False

    for kys in range(len(lc)):
        # if exist change its value
        if lc[kys] == key:
            a_dictionary.__setitem__(lc[kys], value)
            key_found = True

    # if key not found, make a new dict key-value using update({key: value})
    if not key_found:
        a_dictionary.update({key: value})

    return a_dictionary
