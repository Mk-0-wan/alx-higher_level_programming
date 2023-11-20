#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list is not None:
        index = 0
        for elem in my_list:
            try:
                print("{}".format(my_list[elem]), end="")
            except (IndexError):
                print()
                return (index)
            else:
                index += 1
        return index
