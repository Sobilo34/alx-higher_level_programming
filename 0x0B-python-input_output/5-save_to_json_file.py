#!/usr/bin/python3

"""
This is a function that writes an Object to a
text file, using a JSON representation
Prototype: def save_to_json_file(my_obj, filename):
"""


def save_to_json_file(my_obj, filename):
    """
     writes an Object to a text file
     using a JSON representation

     Argumnents:
            my_obj - This is the object to write to text file
            filename - This is the name of the file
    """
    import json

    with open(filename, "w") as the_file:
        the_file.write(json.dumps(my_obj))
