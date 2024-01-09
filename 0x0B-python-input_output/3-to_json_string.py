#!/usr/bin/python3

"""
This is a function that returns the JSON representation of an object (string)
Prototype: def to_json_string(my_obj):
"""


def to_json_string(my_obj):
    """
    Returns the JSON representation of an object
    Argumnent:
            my_obj - The object that will be
            converted to JSON representation
    """
    import json

    output = json.dumps(my_obj)
    return (output)
