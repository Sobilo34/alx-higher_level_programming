#!/usr/bin/python3

def roman_to_int(roman_string):
    if not isinstance(roman_string, str) or roman_string is None:
        return 0

    roman_numerals = {
        'I': 1, 'V': 5, 'X': 10, 'L': 50,
        'C': 100, 'D': 500, 'M': 1000
    }

    output = 0
    old_val = 0

    for numeral in reversed(roman_string):
        current_val = roman_numerals[numeral]
        if current_val >= old_val:
            output += current_val
        else:
            output -= current_val
        old_val = current_val

    return output
