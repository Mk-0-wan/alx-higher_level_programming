#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    new_list = my_list.copy()
    x = len(my_list)
    if idx < 0 and idx > x-1:
        return new_list
    else:
        new_list[idx] = int(element)
        return new_list
