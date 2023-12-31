#!/usr/bin/python3
def best_score(a_dict):
    """
    Returns the key with the highest integer value
    """
    if a_dict is None or a_dict == {}:
        return None
    best = max(a_dict.values())
    for key in a_dict.keys():
        if a_dict[key] == best:
            return key
