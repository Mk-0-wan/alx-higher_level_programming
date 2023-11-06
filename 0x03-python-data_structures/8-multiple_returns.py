#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        ch = None
    else:
        ch = sentence[0]
    return int(len(sentence)), ch
