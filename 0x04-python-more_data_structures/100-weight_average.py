#!/usr/bin/python3
def weight_average(my_list=[]):
    if not my_list:
        return 0

    products = sum(score * weight for score, weight in my_list)
    weights = sum(weight for _, weight in my_list)

    return products / weights
