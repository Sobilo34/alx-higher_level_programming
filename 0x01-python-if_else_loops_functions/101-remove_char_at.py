#!/usr/bin/python3
def remove_char_at(str, n):
    result_str = ""
    for count in range(len(str)):
        if (count == n):
            continue
        result_str += str[count]

    return result_str
