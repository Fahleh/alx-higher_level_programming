#!/usr/bin/python3

def add_tuple(a=(), b=()):
    """
    Add the first elemnts of a & b
    if a tuple is less than 2,
    0 is used for the missing integer,
    if more than 2, the first 2 are used
    Args:
        a - Tuple
        b - Tuple
    Return:
        (c, d)
    """
    while len(a) < 2:
        a = (*a, 0)
    while len(b) < 2:
        b = (*b, 0)
    return a[0] + b[0], a[1] + b[1]


if __name__ == '__main__':
    a = (1, 89)
    b = (88, 11)
    print(add_tuple(a, b))
    print(add_tuple(a, (1,)))
    print(add_tuple(a, ()))
