#!/usr/bin/python3

def update_dictionary(a_dict, key, value):
    """
    Replaces or adds a new key/value in 
    a dictionary.
    """
    if a_dict is None:
        return None
    a_dict[key] = value
    return a_dict
