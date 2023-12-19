#!/usr/bin/python3

"""This is to define MagicClass matching bytecode"""
import math


class MagicClass:
    """
    Initialize and define methods area and circumference
    to represent a circle.
    """
    def __init__(self, radius=0):
        self.__radius = 0

        #  verify that radius is a number
        if not isinstance(radius, (int, float)):
            raise TypeError("radius must be a number")
        #  update attribute
        self.__radius = radius

    def area(self):
        return self.__radius ** 2 * math.pi

    def circumference(self):
        return 2 * math.pi * self.__radius
