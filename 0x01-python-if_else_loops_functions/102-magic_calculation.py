#!/usr/bin/python3

def magic_calculation(x, y, z):
    if x < y:
        return z
    if z > y:
        return x + y
    return (x * y) - z
