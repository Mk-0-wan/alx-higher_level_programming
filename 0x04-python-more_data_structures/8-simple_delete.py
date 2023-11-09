#!/usr/bin/python3
def simple_delete(a_dictionary, key=""):
    # delete a key at a given position
    lc = list(a_dictionary.keys())

    for kys in range(len(lc)):
        if lc[kys] == key:
           a_dictionary.pop(lc[kys])
           return a_dictionary
    # if the key doesn't exist just return the original dict
    return a_dictionary
