#!/usr/bin/python3

"""
This is a function that adds all arguments to a
python list, and then save them to a file
Must use your function save_to_json_file from 5-save_to_json_file.py
Must use your function load_from_json_file from 6-load_from_json_file.py
"""


from sys import argv
import json

if __name__ == "__main__":
    save_to_json_file = __import__('5-save_to_json_file').save_to_json_file

    load_from_json_file = \
        __import__('6-load_from_json_file').load_from_json_file

    try:
        add_item_data = load_from_json_file("add_item.json")

        loaded_data = add_item_data + argv[1:]

    except (FileNotFoundError, json.JSONDecodeError):
        add_item_data = []
        loaded_data = argv[1:]

    save_to_json_file(loaded_data, "add_item.json")
