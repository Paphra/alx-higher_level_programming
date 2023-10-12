#!/usr/bin/python3
"""8-class_to_json module

Contains a function that returns a dict desc of a class
For JSON serialization
"""


def class_to_json(obj):
    """Returns a dict description with simple data structures
    """

    return obj.__dict__
