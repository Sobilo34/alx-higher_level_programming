#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    '''
    function that prints x elements of a list.
    '''
    count = 0
    try:
        for index in range(x):
            print("{}".format(my_list[i]), end="")
            count += 1
    except IndexError:
        pass
    finally:
        print()
        return count
