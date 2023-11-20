#!/usr/bin/python3
def recursive_len(seq):
    if not seq:
        return (0)
    else:
        return (1 + recursive_len(seq[1:]))


def safe_print_list(my_list=[], x=0):
    try:
        i = 0
        while i < x:
            print("{:d}".format(my_list[i]), end=("", "\n")[i >= x-1])
            i = i + 1
        return (i)
    except (IndexError):
        y = int(recursive_len(my_list))
        print()
        return (y)
