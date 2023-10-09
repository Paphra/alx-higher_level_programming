#!/usr/bin/python3
"""101-add_attribute module

Contains a function that adds a new attrbute to a class if possible
"""


def add_attribute(cls, attr, value):
    """Adds a new attribute if possible
    """

    if '__dict__' not in dir(cls):
        raise TypeError("can't add new attribute")
    setattr(cls, attr, value)
