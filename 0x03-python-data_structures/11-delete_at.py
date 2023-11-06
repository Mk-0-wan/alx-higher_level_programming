#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if len(my_list) == 0:
        return None
    elif 0 < idx or idx > len(my_list)-1:
        return my_list
    else:
        my_list = my_list[:idx] + my_list[idx+1:]
        return my_list
