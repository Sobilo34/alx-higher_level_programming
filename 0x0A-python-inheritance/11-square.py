#!/usr/bin/python3
"""
a class Square that inherits from Rectangle (9-rectangle.py)
(task based on 10-square.py)
"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    This is a class representing a square
    """

    def __init__(self, size):
        """
        This is to initializes a square with the given size 

        Args:
            size (int): The size of the square.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """
        Returns:
            str: [Square] <size>/<size>
        """
        return "[Square] {}/{}".format(self.__size, self.__size)
