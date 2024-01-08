#!/usr/bin/python3
"""
This returns True if the object is exactly an instance of the
specified class ; else, it return False.
"""


def is_same_class(obj, a_class):
    """
        This is the function that returns True if the object is exactly
                        an instance of the specified class ; else, it returns False.

        Arguements:
            obj: An object of instance-- of the class
            a_class: The class.

        Return: Return true if otherwise return false
    """
    return (type(obj) is a_class)
