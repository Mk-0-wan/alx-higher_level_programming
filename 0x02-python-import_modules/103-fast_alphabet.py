#!/usr/bin/python3
call = lambda start, stop: print(*list(map(chr, range(start, stop))), sep="", end="\n")
call(65, 91)
