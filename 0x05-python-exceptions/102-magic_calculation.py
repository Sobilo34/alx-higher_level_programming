#!/usr/bin/python3

def magic_calculation(a, b):
    output = 0

    for i in range(1, 3):
        try:
            if i > a:
                raise Exception('Too far')
            output = output + (a ** b) / i

        except Exception:
            output = b + a
            break

    return (output)
