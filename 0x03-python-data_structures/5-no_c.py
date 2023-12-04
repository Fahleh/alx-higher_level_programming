#!/usr/bin/python3

def no_c(my_str):
    """
    Removes all charactrs  c and C
    Args:
        my_str - String to edit.
    """
    return "".join(filter(lambda x: x not in 'cC', my_str))
