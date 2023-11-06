#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    start_val = int(my_list[0])
    for i in my_list[1:]:
        if (i > start_val):
            start_val = int(i)
    return (start_val)
