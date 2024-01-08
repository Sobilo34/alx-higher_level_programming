#!/usr/bin/python3

"""
This is a class that inherits properties and attributes from `list`
"""


class MyList(list):
    """
    This class will inherit the list
    Methods: print_sorted(self)
    """
    def __init__(self):
        """initializer for MyList"""
        super().__init__()

    def print_sorted(self):
        """prints the list(sorted) in ascending order
        type(int)
        """
        print(sorted(self))
