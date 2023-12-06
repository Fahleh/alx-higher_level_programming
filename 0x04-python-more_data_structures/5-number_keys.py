#!/usr/bin/python3
def number_keys(a_dict):
    """
    Returns the number of keys in a
    dictionary
    """
    if a_dict is None:
        return None
    return len(a_dict.keys())
