#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if len(my_list) == 0:
        return None
    elif idx < 0 and idx > x-1:
        return None
    else:
        new_list = my_list.copy()
        new_list[idx] = element
        return new_list
