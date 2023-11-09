#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    # first retrive the elements in the dict
    lc = list(a_dictionary.keys())
    # sort the dict key
    lc.sort()
    for kys in range(len(lc)):
        # collect the values from the dict
        vals = a_dictionary.get(lc[kys])
        # dict keys should be string formatted
        print("{:s}: {}".format(lc[kys], vals))
    """
    for elements in lc:
        for i in range(len(elements)):
            print("{}".format(elements[i]), end=(': ', "\n")[i == len(elements)-1])
   
    # value can be of any value
    """
    return None
