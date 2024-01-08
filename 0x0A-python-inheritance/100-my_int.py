#!/usr/bin/python3

"""
a class MyInt that inherits from int
"""


class MyInt(int):
    """
    This is the class int that will
    define a class that inverts == !=. operators
    """

    def __eq__(self, other):
        """initialize"""
        if int.__ne__(self, other):
            return True
        else:
            return False

    def __ne__(self, other):
        """intializer for greater than"""
        if int.__eq__(self, other):
            return True
        else:
            return False
