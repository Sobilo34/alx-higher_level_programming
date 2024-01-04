#!/usr/bin/python3
"""
a class Write a class Rectangle that defines a rectangle by: (based on 2-rectangle.py)
"""


class Rectangle:
    """
    The instantaitin point
    """
    def __init__(self, width=0, height=0):
        """ __init__ method to initialize the attributes of the class"""
        if type(width) is not int:
            raise TypeError("width must be an integer")
        elif width < 0:
            raise ValueError("width must be >= 0")
        self.__width = width

        if type(height) is not int:
            raise TypeError("height must be an integer")
        elif height < 0:
            raise ValueError("height must be >= 0")
        self.__height = height

    @property
    def width(self):
        """ to retrieve width """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ to retrieve height """
        return self.__height

    @height.setter
    def height(self, value):
        """ sets the value of the height if all conditions are met """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """public instance attribute that returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """ calculates the perimeter of the rectangle """
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ prints the output """
        if self.__width == 0 or self.__height == 0:
            return ""
        _str = ""
        for counter in range(self.height):
            _str = _str + "#" * self.width + "\n"
        return _str.rstrip() 
