#!/usr/bin/python3
numbers = list(range(65, 91))
print(*list(map(chr, numbers)), sep="", end="\n")
