#!/usr/bin/python3
def remove_char_at(str, n):
    str_output = ""
    for count in range(len(str)):
        if (count == n):
            continue
        str_output += str[count]

    return str_output
