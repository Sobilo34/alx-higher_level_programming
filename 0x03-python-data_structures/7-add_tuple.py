#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    a = tuple_a or (0, 0)
    b = tuple_b or (0, 0)
    length1 = len(a)
    length2 = len(b)

    if (length1 == 1):
        a = (tuple_a[0], 0)
    if (length2 == 1):
        b = (tuple_b[0], 0)
    return ((a[0] + b[0], a[1] + b[1]))
