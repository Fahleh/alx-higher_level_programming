#!/usr/bin/python3
def _get_value(char):
    """
    Returns the roman equivalent of a number
    Nothing if its not a Roman Character
    """
    romans = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 100
    }
    char = char.upper()
    if char in romans:
        return romans[char]
    return None


def roman_to_int(roman):
    """
    Converts Roman numerals to Decimal
    Args:
        roman - String of roman numerals
    """

    if not isinstance(roman, str) or roman is None:
        return 0

    res, prev, curr = 0, 0, 0

    for c in roman:
        curr = _get_value(c)
        if curr is None:
            raise ValueError("Wrong input")
        if curr > prev:
            res -= prev
            curr -= prev
        res += curr
        prev = curr

    return res
