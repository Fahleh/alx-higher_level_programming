#!/usr/bin/python3
"""
A function that returns a list of lists of integers
representing the Pascal’s triangle.
"""


def pascal_triangle(n):
    """
    Represent Pascal's Triangle of size n.
    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    pascals_triangle = [[1]]
    while len(pascals_triangle) != n:
        triangle = pascals_triangle[-1]
        temp = [1]
        for i in range(len(triangle) - 1):
            temp.append(triangle[i] + triangle[i + 1])
        temp.append(1)
        pascals_triangle.append(temp)
    return pascals_triangle
