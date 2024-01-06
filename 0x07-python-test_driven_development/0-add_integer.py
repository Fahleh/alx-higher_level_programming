#!/usr/bin/python3
"""A function for adding two numbers."""


def add_integer(a, b=98):
    """Returns the integer sum of a and b.
    Float arguments are typecasted to integers before addition.
    Raises:
        TypeError: If either of a or b is a non-integer and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")
    return (int(a) + int(b))
