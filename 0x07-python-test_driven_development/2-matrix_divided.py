#!/usr/bin/python3
"""
2-matrix_divided module

Contains a function that divides all elements of a matrix.
"""


def matrix_divided(matrix, div):
    """
    Returns a new matrix after dividing the elements by div
    """

    if type(matrix) is not list:
        raise TypeError(
            'matrix must be a matrix (list of lists) of \
                    integers/floats'
            )
    size = 0
    num_rows = 0
    for row in matrix:
        if type(row) is not list:
            raise TypeError(
                'matrix must be a matrix (list of lists) of'
                + ' integers/floats'
            )
        if len(row) != size and num_rows > 0:
            raise TypeError(
                'Each row of the matrix must have the same size'
            )
        for i in row:
            if type(i) is not int and type(i) is not float:
                raise TypeError(
                    'matrix must be a matrix (list of lists)'
                    + ' of integers/floats'
                )

        if num_rows == 0:
            size = len(row)
        num_rows += 1

    if type(div) is not int and type(div) is not float:
        raise TypeError('div must be a number')
    if div == 0:
        raise ZeroDivisionError('division by zero')

    new_matrix = []
    for row in matrix:
        new_row = []
        for i in row:
            new_row.append(round(i/div, 2))
        new_matrix.append(new_row)

    return new_matrix
