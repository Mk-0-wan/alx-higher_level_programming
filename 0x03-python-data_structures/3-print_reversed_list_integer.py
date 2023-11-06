#!/usr/bin/python3
if __name__ != "__main__":
    def print_reversed_list_integer(my_list=[]):
        """
        prints the reverse order of a list
        """
        last = len(my_list)+1

        for i in range(1, last):
            i *= -1
            print("{:d}".format(int(my_list[i])))
