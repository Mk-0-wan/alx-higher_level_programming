#!/usr/bin/python3
def search_replace(my_list, search, replace):
    lc = my_list.copy()
    for i, elements in enumerate(lc):
        if search == elements:
            lc[i] = replace
    return lc
