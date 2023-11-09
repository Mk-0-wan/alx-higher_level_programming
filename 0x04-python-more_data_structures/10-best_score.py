#!/usr/bin/python3
def max_integer(my_list=[]):
    if len(my_list) == 0:
        return None
    start_val = int(my_list[0])
    for i in my_list[1:]:
        if (i > start_val):
            start_val = int(i)
    return (start_val)

def best_score(a_dictionary):
    if a_dictionary is None:
        return None
    lc = list(a_dictionary.keys())
    max_score = []

    for kys in range(len(lc)):
        if (a_dictionary.get(lc[kys]) != None):
            max_score.append(a_dictionary.get(lc[kys]))
    
    max_value = max_integer(max_score)

    for new_kys in range(len(lc)):
        if (max_value == a_dictionary.get(lc[new_kys])):
            return lc[new_kys]
    #return None