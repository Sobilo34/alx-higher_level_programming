#!/usr/bin/python3
"""Write a class Rectangle that defines a rectangle by:
    (based on 8-rectangle.py"""


class Rectangle:
    """width and height attributes"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @classmethod
    def square(cls, size=0):
        """makes new square"""
        return (cls(size, size))

    @property
    def width(self):
        """gets width"""
        return self.__width

    @width.setter
    def width(self, value):
        """sets value"""

        if not isinstance(value, int):
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')
        self.__width = value

    @property
    def height(self):
        """gets height"""

        return self.__height

    @height.setter
    def height(self, value):
        """sets height"""
        if not isinstance(value, int):
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')
        self.__height = value

    def area(self):
        """return area of a rectangle"""
        return self.width * self.height

    def perimeter(self):
        """return perimeter of rectangle"""
        if self.width == 0 or self. height == 0:
            return 0
        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        """mod string object"""
        if self.height == 0 or self.width == 0:
            return ""
        return ('\n'.join("{}".format(
            self.print_symbol) * self.width for i in range(self.height)))

    def __repr__(self):
        """show way to replicate the class"""
        return ("Rectangle({}, {})".format(self.width, self.height))

    def __del__(self):
        """detect when class is deleted"""
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    def bigger_or_equal(rect_1, rect_2):
        """return bigger area"""
        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() >= rect_2.area():
            return rect_1
        return rect_2
