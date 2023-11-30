#!/usr/bin/python3

import importlib

if __name__ == "__main__":
    _import = importlib.import_module("hidden_4")

    byte = dir(_import)

    for index, the_name in enumerate(byte):
        if the_name[0] == '_':
            continue

        print("{}".format(the_name))
