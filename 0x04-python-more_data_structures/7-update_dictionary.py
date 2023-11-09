def update_dictionary(a_dictionary, key, value):
    # Check if key exists in the dictionary
    if key in a_dictionary:
        # If key exists, update its value
        a_dictionary[key] = value
    else:
        # If key doesn't exist, add a new key-value pair
        a_dictionary[key] = value

    return a_dictionary
