#!/usr/bin/python3

"""
This is to define a class Square that represents a square
"""


class Square:
    """ Square class representing a square"""
    def __init__(self, size=0):
        self._size = 0
        self.size = size

    @property
    def size(self):
        return self._size

    @size.setter
    def size(self, value):
        if not isinstance(value, (float, int)):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    def area(self):
        return self._size ** 2

    def __eq__(self, other):
        return isinstance(other, Square) and self.area() == other.area()

    def __ne__(self, other):
        return isinstance(other, Square) and self.area() != other.area()

    def __lt__(self, other):
        return isinstance(other, Square) and self.area() < other.area()

    def __le__(self, other):
        return isinstance(other, Square) and self.area() <= other.area()

    def __gt__(self, other):
        return isinstance(other, Square) and self.area() > other.area()

    def __ge__(self, other):
        return isinstance(other, Square) and self.area() >= other.area()
