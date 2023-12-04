#!/usr/bin/python3

def new_in_list(my_list, idx, elem):
    """
    Replace an elment in a list at a specified index
    Args:
        my_list - List to search
        idx - Specified index
        elem - Element to insert
    Return:
        modified my_list
    """
    copy = my_list[:]
    if idx < 0 or idx >= len(copy):
        return copy
    copy[idx] = elem
    return copy
