#!/usr/bin/python3

"""
This is a function that appends a string at the end of
a text file (UTF8) and returns the number of characters added
Prototype: def append_write(filename="", text="")
"""


with open(filename, "a", encoding="UTF8") as the_file:
    """
    This function appends a string at the end of the text
    Argument:
            filename - This is the name of the file to append in
            text - This is the test to be appended
    """
    val = the_file.write(text)
    return val
