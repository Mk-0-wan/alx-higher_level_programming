#!/usr/bin/python3
import hidden_4

if __name__ == "__main__":
    for methods in dir(hidden_4):
        if (methods.endswith("__")):
            continue
        else:
            print(methods)
