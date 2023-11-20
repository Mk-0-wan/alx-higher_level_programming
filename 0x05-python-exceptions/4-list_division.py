#!/usr/bin/python3
def list_division(my_list_1, my_list_2, list_length):
    if (my_list_1, my_list_2) is not None:
        index = 0
        new_list = []
        for elem in range(0, list_length):
            try:
                index = my_l_1[elem] / my_l_2[elem]
            except (TypeError):
                index = 0
                print("wrong type")
            except (ZeroDivisionError, FloatingPointError):
                index = 0
                print("division by 0")
            except (IndexError):
                index = 0
                print("out of range")
            finally:
                new_list.append(index)
        return (new_list)
