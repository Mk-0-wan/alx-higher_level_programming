#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    true_or_false_list = []
    for i in range(0, len(my_list)):
        if (my_list[i] % 2 == 0):
            true_or_false_list.append(True)
        else:
            true_or_false_list.append(False)
    return true_or_false_list
