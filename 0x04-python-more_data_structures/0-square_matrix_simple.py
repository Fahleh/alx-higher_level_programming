#!/usr/bin/python3
def square_matrix_simple(matrix=[]):
    """
    Computes the square each element
    in a matrix
    Args:
        matrix - A 2D array.
    """
    if matrix is None:
        return None
    return [
        [x**2 for x in row] for row in matrix
    ]
