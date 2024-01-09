#!/usr/bin/python3

"""
This is a function that returns the dictionary
description with simple data structure
(list, dictionary, string, integer and boolean)
for JSON serialization of an object
Prototype: def class_to_json(obj):
"""


def class_to_json(obj):
    """
    The class json obj
    Argumnet:
            obj - The object
    """
    return obj.__dict__
