#!/usr/bin/python3

"""
a class Rectangle that defines a rectangle by: (based on 0-rectangle.py)
that has been written formally
"""


class Rectangle:
    """
    This is the declaration of the rectangle
    """
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        #This is the property to retrieve the width of the rectangle
        return __self.width

    @width.setter
    def width(self, value):
        #Now we test if the value is an int
        if type(value) is not or isinstance(value, (float, bool):
                raise TypeError("width must be an integer")

        #Now we test if the value is >= 0
        if value < 0:
        raise ValueError("width must be >= 0")

        # Now we update the value of the width
        self.__width = value

    @property
        def height(self):
        #This is the property to retrieve the height of the rectangle
        return __self.height

    @height.setter
    def height(self, value):
        #now we test if value is an integer
        if type(value) is not int:
            raise TypeError("height must be an integer")
    
        #Now we test if the height value is >=0
        if value < 0:
        raise ValueError("height must be >= 0")

        #Then we also update the value of the height
        self.__height = value
