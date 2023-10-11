#!/usr/bin/python3
"""3-to_json_string module

Contains a function that returns the JSON rep of an object
"""


import json


def to_json_string(my_obj):
    """Returns a JSON rep of an object
    """

    return json.dumps(my_obj)
