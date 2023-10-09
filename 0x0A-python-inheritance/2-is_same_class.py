#!/usr/bin/python3
"""2-is_same_class module

Containts a function that checks the instance
"""


def is_same_class(obj, a_class):
    """Checks the object whether it is an instance of a class
    """

    return type(obj) == a_class
