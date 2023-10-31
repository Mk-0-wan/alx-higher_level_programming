#!/usr/bin/python3
#index to keep track of each character position
#start at index 1
index = 1

#enumerate over each character and collect its index
for i, char in enumerate(range(122, 96, -1)):
    #perform an uppercase logic to that char
    #increment index by 2 to have an alternate sequence
    if i == index:
        char -= 32
        index += 2
    print(chr(char), end='')
