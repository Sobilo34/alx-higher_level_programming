#!/usr/bin/python3

"""
program that returns the square of a class
"""


class Square:
    """
    For instantiating the variables and raising error for exeptions
    """
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")

        if value < 0:
            raise ValueError("size must be >= 0")

        self.__size = value

    def area(self):
        """
        To calculate the area of the square
        """
        return (self.__size ** 2)
