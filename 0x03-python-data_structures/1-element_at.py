#!/usr/bin/python3

def element_at(my_list, idx):
    length = len(my_list)
    if 0 <= idx < length:
        return my_list[idx]
    else:
        return None
