#!/usr/bin/python3

def max_integer(my_list=[]):
    """
    Find the biggest integer in a list
    Args:
        my_list - List
    Return:
        None - If list is empty
        Biggest integer in list
    """
    L = len(my_list)
    if L == 0:
        return None
    Max = my_list[0]
    for elem in my_list:
        if elem > Max:
            Max = elem
    return Max
