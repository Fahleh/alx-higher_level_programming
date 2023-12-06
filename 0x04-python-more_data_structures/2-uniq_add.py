#!/usr/bin/python3
def uniq_add(my_list=[]):
    """
    Add all the unique integers in a list
    """
    if my_list is None:
        return None
    return sum(set(my_list))
