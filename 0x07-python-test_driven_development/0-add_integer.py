#!/usr/bin/python3

def add_integer(a, b=98):
    """
    Function that adds two integers.

    Args:
        a (int or float): The first number to add.
        b (int or float, optional): The second number to add (default is 98).

    Raises:
        TypeError: If either `a` or `b` is not an integer or float.

    Returns:
        int: The addition of `a` and `b` as an integer.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer or float")

    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer or float")

    return int(a) + int(b)
