#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    """
    deletes element at a given index
    """
    if 0 > idx or idx >= len(my_list):
        return my_list

    del my_list[idx]
    return (my_list)
