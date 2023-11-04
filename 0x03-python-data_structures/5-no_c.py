#!/usr/bin/python3
def no_c(my_string):
    # first create a list of char to find
    c = ['C', 'c']
    # make a lambda function that returns an index of each ch found
    idx = lambda c, my_string: my_string.find((c[0], c[1])[c[1] in my_string])
    # find the occurrence of the ch char is my_string
    while idx(ch, my_string) != -1:
        index = idx(ch, my_string)
        # modify the string accordingly to exclude the ch chars using slicing
        my_string = my_string[:index] + my_string[index + 1:]
    return (my_string)
