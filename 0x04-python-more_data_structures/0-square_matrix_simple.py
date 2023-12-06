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


if __name__ == '__main__':
    s = square_matrix_simple([
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ])
    print(s)
