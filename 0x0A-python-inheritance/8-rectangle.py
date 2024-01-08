#!/usr/bin/python3

"""
 a class Rectangle that inherits from BaseGeometry (7-base_geometry.py). (task based on 8-rectangle.py
"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    This is the class Rectangle extends from BaseGeometry
    """
    def __init__(self, width, height):
        """
        initializer
        Args:
            width
            height
        """
        super().integer_validator("width", width)
        self.__width = width
        super().integer_validator("height", height)
        self.__height = height
