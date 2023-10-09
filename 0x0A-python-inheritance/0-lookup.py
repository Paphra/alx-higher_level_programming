#!/usr/bin/python3
"""0-lookup module

Contains a function that returns the attrinutes and methods
available on a given object
"""


def lookup(obj):
    """ lookup function

    Args:
        obj (object): the object
    Returns: a list of available attrs and methods
    """

    return dir(obj)
