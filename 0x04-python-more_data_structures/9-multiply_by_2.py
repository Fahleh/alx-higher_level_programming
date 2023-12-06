#!/usr/bin/python3
def multiply_by_2(a_dict):
    """
    Multiply all dictionary values by 2.
    """
    if a_dict is None:
        return None
    return {
        key: a_dict[key] * 2 for key in a_dict
    }
