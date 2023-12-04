#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for a, value in enumerate(row):
            if a == len(row) - 1:
                print("{:d}".format(value), end="")
            else:
                print("{:d} ".format(value), end="")
        print()
