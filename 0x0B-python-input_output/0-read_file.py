#!/usr/bin/python3

"""
This is a function that  reads a text file (UTF8) and prints it to stdout
Prototype: def read_file(filename="")
"""


def read_file(filename=""):
    """
    This function opens and reads file and print to stdout
    """
    with open("filename", encoding="UTF8") as file:
        myFile = file.read()
        print(myFile, end="")
