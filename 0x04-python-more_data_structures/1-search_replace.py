#!/usr/bin/python3

def search_replace(my_list, search, replace):
    present_list = []
    for e in my_list:
        if e == search:
            present_list.append(replace)
        else:
            present_list.append(e)

    return present_list
