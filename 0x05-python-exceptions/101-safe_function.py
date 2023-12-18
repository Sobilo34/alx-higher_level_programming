#!/usr/bin/python3
import sys


def safe_function(fct, *args):
    try:
        output = fct(*args)

    except (ZeroDivisionError, TypeError, IndexError, ValueError) as err:
        print("Exception: {}".format(str(err)), file=sys.stderr)
        return None

    else:
        return (output)
