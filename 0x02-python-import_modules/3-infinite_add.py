#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv

    count = len(argv)
    number = 0

    if count == 1:
        print(int(0))
    if count > 1:
        for index in range(1, count):
            number += int(argv[index])

        result = "{}".format(int (number))
        print(result)
