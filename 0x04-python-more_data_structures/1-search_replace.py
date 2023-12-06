#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """
    Replace all occurences of an element
    in a list
    Args:
        my_list - List to search
        search - Element to replace
        replace - Replacement element
    """
    if my_list is None:
        return None
    return [
        replace if x == search else x for x in my_list
    ]
