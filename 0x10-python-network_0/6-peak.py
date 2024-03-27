#!/usr/bin/python3
"""
    Defines an algorithm to find the peak in a list
    of unsorted numbers.
"""


def find_peak(list_of_integers):
    """Finds a peak in a list of unsorted integers."""
    if list_of_integers == []:
        return None

    length = len(list_of_integers)
    if length == 1:
        return list_of_integers[0]
    elif length == 2:
        return max(list_of_integers)

    left = 0
    right = length - 1

    while left <= right:
        mid = (left + right) >> 1

        if (mid == 0 or list_of_integers[mid - 1]
            <= list_of_integers[mid]) and \
           (mid == length - 1 or list_of_integers[mid + 1]
                <= list_of_integers[mid]):
            return list_of_integers[mid]
        elif mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            right = mid - 1
        else:
            left = mid + 1
