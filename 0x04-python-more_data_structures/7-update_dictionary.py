def update_dictionary(a_dictionary, key, value):
    # find a key in the dict
    lc = list(a_dictionary.keys())

    for kys in range(len(lc)):
        # if exist change its value
        if lc[kys] == key:
            a_dictionary.__setitem__(lc[kys], value)
        # if not then make a new dict key value use update({key: value})
        else:
            a_dictionary.update({key: value})

    return a_dictionary
