#!/usr/bin/python3

def best_score(a_dictionary):
    if not a_dictionary:
        return None
    biggest_int = max(a_dictionary, key=a_dictionary.get)

    return biggest_int
