#!/usr/bin/python3
def recursive_len(seq):
    if not seq:
        return (0)
    else:
        return (1 + recursive_len(seq[1:]))


def safe_print_list(my_list=[], x=0):
    try:
        if (x <= recursive_len(my_list)):
            i = 0
            while i < x:
                print("{}".format(my_list[i]), end=("", "\n")[i == x-1])
                i = i + 1
            return (i)
        else:
            raise (IndexError)
    except (IndexError):
        y = recursive_len(my_list)
        for j in range(0, y):
            print("{}".format(my_list[j]), end=("", "\n")[j == y-1])
        return (y)
