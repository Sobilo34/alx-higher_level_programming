#!/usr/bin/python3

def safe_print_division(a, b):
    output = None

    try:
        output = p / q
    except ZeroDivisionError:
        output = None
    finally:
        print("Inside result: {:}" .format(output))
    return output
