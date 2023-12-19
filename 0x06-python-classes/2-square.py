#!/usr/bin/python3
"""
A class Square that defines a square by: (based on 1-square.py)
"""


class Square:
    """ class Square that defines a square by: """
    def __init__(self, Bilsize=0):
        if type(BilSize) is not int:
            raise TypeError("size must be an integer")
        elif BilSize < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = BilSize
