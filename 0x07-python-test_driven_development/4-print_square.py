#!/usr/bin/python3

"""
This is a function that prints a square with the character #.
"""


def print_square(size):
    """
    This will print a perfect sqaure, given a valid int argument.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    elif size < 0:
        raise ValueError("size must be >= 0")
    elif type(size) is float and size < 0:
        raise TypeError("size must be an integer")
    else:
        for x in range(size):
            print("#" * size)
