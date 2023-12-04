#!/usr/bin/python3

def element_at(my_list, idx):
    """
    Retrieves an element from a list a given index
    Args:
        my_list - List to search
        idx - Index of element
    Return:
        None - If idx is out of range
        Data - Element at idx
    """
    if idx < 0 or idx >= len(my_list):
        return None
    return my_list[idx]
