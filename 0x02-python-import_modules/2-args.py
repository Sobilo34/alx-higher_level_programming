#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    count = len(argv) - 1
    if count == 1:
        string = "argument"
    else:
        string = "arguments"

    if count == 0:
        split_operator = '.'
    else:
        split_operator = ':'

    print("{} {}{}".format(count, string, split_operator))
    for index in range(1, count + 1):
        print("{}: {}".format(index, argv[index]))
