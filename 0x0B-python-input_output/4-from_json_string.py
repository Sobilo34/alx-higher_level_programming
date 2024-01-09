#!/usr/bin/python3

"""
This is a function that  returns an object (Python data structure)
represented by a JSON string
Prototype: def from_json_string(my_str):
"""


def from_json_string(my_str):
    """
    returns an object (Python data structure)
    represented by a JSON string

    Argument:
            my_str - The string to return it JSON
    """
    import json

    the_output = json.load(my_str)
    return the_output
