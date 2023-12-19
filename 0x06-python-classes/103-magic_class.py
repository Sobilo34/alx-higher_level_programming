#!/usr/bin/python3

"""This is to define MagicClass matching bytecode"""


import math

class MagicClass:
    def __init__(self, radius=0):
        if not isinstance(radius, (int, float)):
            raise TypeError('radius must be a number')
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius
