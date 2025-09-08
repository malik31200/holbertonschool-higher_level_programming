#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for index, value in enumerate(row):
            if index != len(row)-1:
                print("{:d}".format(value), end=" ")
            else:
                print("{:d}".format(value), end="")
        print()
