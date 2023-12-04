def new_in_list(my_list, idx, element):
    length = len(my_list)
    if not my_list or idx < 0 or idx >= length:
        return my_list.copy()

    new_list = my_list.copy()
    new_list[idx] = element
    return new_list

