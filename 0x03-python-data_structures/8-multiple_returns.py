#!/usr/bin/python3
def multiple_returns(sentence):
    '''
    returns the length of the string and the first letter
    '''
    if len(sentence) == 0:
        return None

    return int(len(sentence)), sentence[0]
