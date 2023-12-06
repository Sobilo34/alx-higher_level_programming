#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new_dir = {}

    for key, value in a_dictionary.items():
        new_dir[key] = {value * 2}
    return new_dir

