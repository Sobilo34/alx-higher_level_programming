#!/usr/bin/python3
"""
This is a Square class that inherits the rectangle
class, since a square is also a rectangle
Class constructor: def __init__(
self, size, x=0, y=0, id=None):
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """
    Initializes the class square, inherites from rectangle class
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return "[Square] ({}) {}/{} - {}".format(
            self.id, self.x, self.y, self.width)

    @property  # getter decorates the size method as a property
    def size(self):
        return self.height  # Here, height represent size, a side of square

    @size.setter
    def size(self, val):
        self.width = val
        self.height = val

    def update(self, *args, **kwargs):
        """
        This is to assign attributes to the instance
        with argumnent *args and key_value **kwargs
        """
        if args:
            attributes = ['id', 'size', 'x', 'y']
            for loop, arg in enumerate(args):
                setattr(self, attributes[loop], arg)
        elif kwargs:
            for key_value, index in kwargs.items():
                setattr(self, key_value, index)

    def to_dictionary(self):
        """
        This returns the dictionary representation of a Square
        """
        return {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y
        }
