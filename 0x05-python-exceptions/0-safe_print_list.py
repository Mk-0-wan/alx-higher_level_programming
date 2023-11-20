#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    if my_list is not None:
        index = 0
        for elem in range(0, x):
            try:
                print("{}".format(my_list[elem]), end="")
                index += 1
            except:
                continue
        print()
        return index
