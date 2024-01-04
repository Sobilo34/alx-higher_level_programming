#!/usr/bin/python3

"""
a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
that has been written formerly
"""


class Rectangle:
    """
    This is the declaration of the rectangle

    Args:
        width (int)
        height (int)
    """
    def __init__(self, width=0, height=0):
        self.height = height
        self.width = width

    @property
    def width(self):
        #This is the property to retrieve the width of the rectangle
        return self.__width

    @width.setter
    def width(self, value):
        # verify that value is an integer
        if type(value) is not int:
            raise TypeError("width must be an integer")

        # check that value is >= 0
        if value < 0:
            raise ValueError("width must be >= 0")

        # update private instance attribute
        self.__width = value

    @property
    def height(self):
        # property to retreive height
        return self.__height

    @height.setter  # setter method for height
    def height(self, value):
        # verify that value is an integer
        if type(value) is not int:
            raise TypeError("height must be an integer")

        # check if value is >= 0
        if value < 0:
            raise ValueError("height must be >= 0")

        # update private instance attribute
        self.__height = value
