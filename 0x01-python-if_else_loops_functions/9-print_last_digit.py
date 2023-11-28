#!/usr/bin/python3
def print_last_digit(the_digit):
    if the_digit < 0:
        the_digit = the_digit * -1
        the_digit = the_digit % 10
        print(the_digit, end='')
    else:
        the_digit = the_digit % 10
        print(the_digit, end='')
    return (the_digit)
