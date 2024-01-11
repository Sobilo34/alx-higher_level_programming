#!/usr/bin/python3
"""
Module: 1-my_list
Contains the definition of the MyList class.
"""


class MyList(list):
    """
    A class that inherits from the list class with additional functionality.
    """

    def __init__(self):
        """
        To initialize a new instance of MyList.
        """
        super().__init__()

    def print_sorted(self):
        """
        The function prints the list, but sorted in ascending order.
        """
        print(sorted(self))
