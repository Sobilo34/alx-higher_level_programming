#!/usr/bin/python3
"""
This is  a function that prints My name is <first name> <last name>

"""


def say_my_name(first_name, last_name=""):
    """
    This is the function that Prints the formatted name
    "My name is <first_name> <last_name>"

    Args:
        first_name (str): First name to be included in the formatted string.
        last_name (str, optional): Last name. Defaults to "".

    Raises:
        TypeError: If first_name or last_name is not a string.

    Returns:
        None
    """
    # This is to check if first_name is a string raise TypeError if not
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")

    # This is to check if last_name is a string and raise TypeError if not
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")

    # This is to format and print the formatted name
    formatted_name = "My name is {} {}".format(first_name, last_name)
    print(formatted_name)
