#!/usr/bin/python3
def recursive_len(seq):
    if not seq:
        return (0)
    else:
        return (1 + recursive_len(seq[1:]))


def safe_print_list_integers(my_list=[], x=0):
    # all integers should be printed in the same line
    # only integers should be printed
    # if x is greater than the expected raise an exception
    # return the real number of integers printed
    # don't handle the error for printing above the index
    try:
        count = 0
        for i in range(0, x):
            if (isinstance(my_list[i], int)):
                print("{:d}".format(my_list[i]), end="")
                count = count + 1
            elif (isinstance(my_list[i], (list, str))):
                continue
        print()
        return (count)
    except (IndexError) as Id:
        print(Id)

my_list = [1, 2, 3, 4, 5]
nb_print = safe_print_list_integers(my_list, 2)
print("nb_print: {:d}".format(nb_print))

my_list = [1, 2, 3, "School", 4, 5, [1, 2, 3]]
nb_print = safe_print_list_integers(my_list, len(my_list))
print("nb_print: {:d}".format(nb_print))
nb_print = safe_print_list_integers(my_list, len(my_list) + 2)
print("nb_print: {:d}".format(nb_print))
