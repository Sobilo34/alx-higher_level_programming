#!/usr/bin/python3

"""
This is a function that adds all arguments to a
python list, and then save them to a file
Must use your function save_to_json_file from 5-save_to_json_file.py
Must use your function load_from_json_file from 6-load_from_json_file.py
"""


arg_length = len(sys.argv)  # to check number of cmd line args

try:
    # load exixting data from add-item.json
    my_list = load_from_json_file('add_item.json')
except FileNotFoundError:
    my_list = []  # initialize empty list if it doesn't exist

for x in range(1, arg_length):
    # append args to my_list
    my_list.append(sys.argv[x])
# update my_list with data from add-item.json
save_to_json_file(my_list, 'add_item.json')
