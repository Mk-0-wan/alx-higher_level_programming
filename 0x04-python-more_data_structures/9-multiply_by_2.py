#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    # MAKE A COPY FIRST TO RETURN THE NEW DICT
    new_dict = a_dictionary.copy()
    # collect each value
    lv = list(new_dict.keys())
    for kys in range(len(lv)):
        new_value = int(new_dict.get(lv[kys])) * 2
        #print("{:d}".format(int(new_value)))
        new_dict.__setitem__(lv[kys], new_value)
    return new_dict
