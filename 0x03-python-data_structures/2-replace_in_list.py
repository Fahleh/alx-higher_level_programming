#!/usr/bin/python3

def replace_in_list(my_list, idx, elem):
    """
    Replace an elment in a list at a given index
    Args:
        my_list - List to search
        idx - Index of element
        elem - Element to replace witth
    Return:
        my_list
    """
    if idx < 0 or idx >= len(my_list):
        return my_list
    my_list[idx] = elem
    return my_list
