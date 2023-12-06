#!/usr/bin/python3
def only_diff_elements(set_1, set_2):
    """
    Returns a set of all elements present
    in a set.
    Args:
        set_1 - Set one
        set_2 - Set two
    """
    return set_1.symmetric_difference(set_2)
