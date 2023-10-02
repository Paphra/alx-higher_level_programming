#!/usr/bin/python3
"""
A program that solves the N queens problem.

The N queens puzzle is the challenge of placing
N non-attacking queens on an N×N chessboard.
"""


import sys


def solution():
    """
    Solution to the N-queens prob
    """

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

    board = [-1] * N
    place_queens(board, 0)


def place_queens(board, row):
    """
    Place the queens
    """

    N = len(board)

    if row == N:
        print_solution(board)
        return

    for col in range(N):
        if is_safe(board, row, col):
            board[row] = col
            place_queens(board, row + 1)


def is_safe(board, row, col):
    """
    Is it safe to print and fill row
    """

    for i in range(row):
        if board[i] == col:
            return False
        if board[i] - i == col - row or board[i] + i == col + row:
            return False
    return True


def print_solution(board):
    """
    Print the solution
    """

    sol = []
    for i, col in enumerate(board):
        sol.append([i, col])
    print(sol)


if __name__ == '__main__':
    solution()
