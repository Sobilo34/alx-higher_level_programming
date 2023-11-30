#!/usr/bin/python3

if __name__ == "__main__":
    import hidden_4

    index = dir(hidden_4)

    for index, the_name in enumerate(index):
        if the_name[0] == '_':
            continue
        else:
            print("{}".format(the_name))
