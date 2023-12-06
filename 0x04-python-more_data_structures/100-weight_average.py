#!/usr/bin/python3
def weight_average(my_list=[]):
    """
    Find the weighted average of all
    integers in a tuple
    """
    if not my_list:
        return 0
    else:
        return (sum(a * b for a, b in my_list) / sum(b for a, b in my_list))
