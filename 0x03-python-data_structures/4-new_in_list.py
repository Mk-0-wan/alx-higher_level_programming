#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    x = len(my_list)
    if idx < 0 and idx > x-1:
        return None
    else:
        new_list = my_list.copy()
        new_list[idx] = int(element)
        return new_list
