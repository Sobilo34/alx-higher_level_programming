#!/usr/bin/python3

def weight_average(my_list=[]):
    if not my_list:
        return 0

    number = 0
    den= 0

    for tupul in my_list:
        number = number + tupul[0] * tupul[1]
        den = den + tupul[1]

    return (number / den)

