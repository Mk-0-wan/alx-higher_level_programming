#!/usr/bin/python3

def uppercase(str):
    for char in str:
        num_char = ord(char)
        if (97 <= num_char <= 122):
            num_char -= 32
        print(chr(num_char), end='')
    print()
