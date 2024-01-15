#!/usr/bin/python3

"""
This is a Function that adds 2 integers
prototype: def add_integer(a, b=98):
Returns an integer: the addition of a and b
"""


def add_integer(a, b=98):
    """
    function that adds two integers.
    Args:
        a (int or float): The first number to add
        b (int or float, optional): The second number to add(Default at 98)
        Raises:
        TypeError: If either `a` or `b` is not an integer or float.
        Returns:
        int: The addition of `a` and `b` as an integer.
        """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    # cast numbers into integers if they are float    a = int(a)
    b = int(b)

    return (int(a) + int(b))
