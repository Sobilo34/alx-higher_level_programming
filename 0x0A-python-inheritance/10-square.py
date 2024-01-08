#!/usr/bin/python3

"""
a class Square that inherits from Rectangle (9-rectangle.py)
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """This is a square class"""

    def __init__(self, size):
        """This is to initialize the class
        Args
           size: size of side of square
        """
        super().integer_validator('size', size)
        Rectangle.__init__(self, size, size)
