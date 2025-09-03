#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    count = len(argv) - 1
    if count == 0:
        print("0")
    else:
        total = 0
        for i in argv[1:]:
            total = total + int(i)
        print(total)
