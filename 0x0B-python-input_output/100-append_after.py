#!/usr/bin/python3
"""
This is a function that inserts a line of text to a file,
after each line containing aspecific string
"""


def append_after(filename="", search_string="", new_string=""):
    """
    Declaration of the funtion
    """
    with open(filename, 'r') as file:
        lines = file.readlines()

    with open(filename, 'w') as file:
        for line in lines:
            file.write(line)
            if search_string in line:
                file.write(new_string)
