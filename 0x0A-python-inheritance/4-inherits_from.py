#!/usr/bin/python3
"""4-inherits_from module

Checks whether a given object inherits from a class
"""


def inherits_from(obj, a_class):
    """Checks inheritance from another class
    """

    if type(obj) is a_class:
        return False
    return isinstance(obj, a_class)
