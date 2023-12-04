#!/usr/bin/python3

def max_integer(my_list=[]):
    if not my_list:
        return None

    maxim = my_list[0]
    for count in my_list:
        if count > maxim:
            maxim = count

    return maxim
