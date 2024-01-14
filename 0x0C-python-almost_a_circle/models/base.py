#!/usr/bin/python3

"""
This is a the base class for all other classes in this module.
class constructor: def __init__(self, id=None):
"""


class Base:
    """
    This is the base class
    """
    __nb_objects = 0 # Initializes the private class attribute

    def __init__(self, id=None):
        if id is not None:
            """Assign the public instance attribute
            id with the argument value
            """
            self.id = id
        else:
            """
            Otherwise, increment __nb_objects and assign new
            value to the public instance attribute id
            """
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects
