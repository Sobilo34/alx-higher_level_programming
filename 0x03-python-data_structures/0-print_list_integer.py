#!/usr/bin/python3

def print_list_integer(my_list=[]):
    length = len(my_list)
    for count in range(length):
        print("{:d}".format(my_list[count]))
