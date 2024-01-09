#!/usr/bin/python3

"""
This is  a function that creates an Object from a “JSON file”
Prototype: def load_from_json_file(filename):
"""


def load_from_json_file(filename):
    """
    This is  a function that creates an Object from a “JSON file"
    Argument:
            filemane - Name of the file to create object in
    """
    import json

    with open(filename, "w") as the_file:
        output = json.loads(the_file))
        return (output)
