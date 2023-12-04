#!/usr/bin/python3

def print_reversed_list_integer(my_list=[]):
    length = len(my_list)
    for count in reversed(length):
        print("{:d}".format(count))

