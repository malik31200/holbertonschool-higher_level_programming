#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    count = len(argv) - 1
    if count == 0:
        print("0 arguments.")
    i = 1
    for value in argv[1:]:
        print("{}: {}".format(i, value))
        i += 1
