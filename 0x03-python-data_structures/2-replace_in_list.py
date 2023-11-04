#!/usr/bin/python3
# modifying a list element
# if the indx is out of rang return the original list
# if the indx is less than 0 return the original list
def replace_in_list(my_list, idx, element):
    x = len(my_list)
    if idx < 0 or idx > x-1:
        return my_list
    else:
        my_list[idx] = int(element)
        return my_list
