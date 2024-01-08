#!/usr/bin/python3

"""
THis is  a function that adds a new attribute to an object if it’s possible
"""


def add_attribute(obj, attr, value):
    """
    This is a funtion that adds attribute if possible
    Args:
       obj
       name
       value
    Return: error (if not possible)
    """
    if not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)
