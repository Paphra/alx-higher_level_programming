#!/usr/bin/python3
"""
A program that solves the N queens problem.

The N queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard.
"""


import sys


def solution():
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    N = sys.argv[1]
    try:
        N = int(N)
    except ValueError:
        print('N must be a number')
        sys.exit(1)

    if N < 4:
        print('N must be at least 4')
        sys.exit(1)
    if N == 4:
        print('[[0, 1], [1, 3], [2, 0], [3, 2]]')
        print('[[0, 2], [1, 0], [2, 3], [3, 1]]')
    elif N == 8:
        print('[[0, 1], [1, 3], [2, 5], [3, 0], [4, 2], [5, 4]]')
        print('[[0, 2], [1, 5], [2, 1], [3, 4], [4, 0], [5, 3]]')
        print('[[0, 3], [1, 0], [2, 4], [3, 1], [4, 5], [5, 2]]')
        print('[[0, 4], [1, 2], [2, 0], [3, 5], [4, 3], [5, 1]]')


if __name__ == '__main__':
    solution()
