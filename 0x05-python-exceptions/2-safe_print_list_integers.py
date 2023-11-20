#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    # all integers should be printed in the same line
    # only integers should be printed
    # if x is greater than the expected raise an exception
    # return the real number of integers printed
    # don't handle the error for printing above the index
    if (my_list is not None):
        index = 0
        for elem in range(0, x):
            if (isinstance(my_list[elem], int)):
                try:
                    print("{:d}".format(my_list[elem]), end="")
                    index += 1
                except (IndexError) as exc:
                    raise exc
        print()
        return (index)
