#!/usr/bin/python3
"""12-pascal_triangle module

Contains a function that returns a list of lists of integers
Representing a Pascal's triangle of n
"""


def pascal_triangle(n):
    """Returns a pasccals triangle of n

    Args:
        n (int): an integer
    Returns: a list of lists of integers
    """

    if n <= 0:
        return []
    pascal = [[1]]
    for i in range(1, n):
        prev = pascal[-1]
        new = [1]

        for j in range(1, len(prev)):
            new.append(prev[j-1] + prev[j])
        new.append(1)
        pascal.append(new)

    return pascal
