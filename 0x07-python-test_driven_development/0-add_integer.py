#!/usr/bin/python3
"""
0-add_integer module

Contains a function for adding two integers
"""


def add_integer(a, b=98):
    """
    Adds two integers

    Args:
        a (int): first integer or float
        b (int): second integer or float, default=98
    Returns: addition of the two
    """
    
    if type(a) is not int and type(a) is not float:
        raise TypeError('a must be an integer')
    if type(b) is not int and type(b) is not float:
        raise TypeError('b must be an integer')
    if type(a) is float:
        a = int(a)
    if type(b) is float:
        b = int(b)

    return a + b
