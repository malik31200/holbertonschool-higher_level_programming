#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    count = len(argv) - 1
    if count == 0:
        print("0 arguments.")
    elif count == 1:
        print("1 argument:")
        i = 1
        for value in argv[1:]:
            print("{}: {}".format(i, value))
            i += 1
    else:
        print("{} arguments:".format(count))
        i = 1
        for value in argv[1:]:
            print("{}: {}".format(i, value))
            i += 1
