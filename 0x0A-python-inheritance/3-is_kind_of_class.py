#!/usr/bin/python3
"""
returns True if the object is an instance of, or if the object is an instance of a class that inherited from, the specified class ; otherwise False
"""


def is_kind_of_class(obj, a_class):
    """
    This function hecks if object is an instance of,
    or inherited from specified class

    Args:
        obj: The object to check.
        a_class: The specified class to compare with.

    Returns:
        bool: True if obj is an instance of a_class or inherited from a_class,
        False otherwise.
    """
    return isinstance(obj, a_class)
