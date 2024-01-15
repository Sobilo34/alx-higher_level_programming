#!/usr/bin/python3
"""
This is the class Rectangle that inherits from Base
Class constructor: def __init__(self, width,
    height, x=0, y=0, id=None):
"""
from models.base import Base


class Rectangle(Base):
    """
    This class has inherited the Base class
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """
        Initializes the constructor for the rectangle
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def to_dictionary(self):
        """
        To return the dictionary that represents rectangle
        """
        return {
            'id': self.id,
            'width': self.width,
            'height': self.height,
            'x': self.x,
            'y': self.y
        }

    @property  # getter setting width public instance to private
    def width(self):
        result = self.__width
        return result

    @width.setter  # set conditon for validation and error raise for exeption
    def width(self, val):
        if not isinstance(val, int):  # checks is a value is not an integer
            raise TypeError("width must be an integer")
        elif val <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = val

    @property  # getter setting height public instance to private
    def height(self):
        result = self.__height
        return result

    @height.setter  # set condition to validate and error raise for execption
    def height(self, val):
        if not isinstance(val, int):
            raise TypeError("height must be an integer")
        elif val <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = val

    @property  # getter set x public instance to private
    def x(self):
        return self.__x

    @x.setter  # set condition for validication and raise error foe execption
    def x(self, val):
        if not isinstance(val, int):
            raise TypeError("x must be an integer")
        elif val < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = val

    @property  # getter y set public isntance to private
    def y(self):
        return self.__y

    @y.setter  # set the condition to validate and raise error for exeption
    def y(self, val):
        if not isinstance(val, int):
            raise TypeError("y must be an integer")
        elif val < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = val

    def area(self):
        """
        A function that return the area of the rectangle
        """
        area_result = self.width * self.height
        return area_result

    def display(self):
        """
        This function that prints in stdout the
        Rectangle instance with the character #
        taking care of x and y cases
        """
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)
        print()

    def __str__(self):
        """
        This function Update the class Rectangle
        by overriding the __str__ method so that it
        returns [Rectangle] (<id>) <x>/<y> - <width>/<height>
        """
        return "[Rectangle] ({}) {}/{} - {}/{}".format(
            self.id, self.x, self.y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """
        This function assign an argument *args to the
        rectangle together with key value **kwargs
        """
        if args:
            attributes = ['id', 'width', 'height', 'x', 'y']
            for loop, arg in enumerate(args):
                setattr(self, attributes[loop], arg)
        elif kwargs:
            for key_value, index in kwargs.items():
                setattr(self, key_value, index)
