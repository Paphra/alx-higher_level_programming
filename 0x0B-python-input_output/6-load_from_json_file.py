#!/usr/bin/python3
"""6-load_from_json_file module

Contains a function that creates an obj from JSON file
"""


import json


def load_from_json_file(filename):
    """Creates an object from a JSON file
    """

    data = ''
    with open(filename, 'r') as f:
        data = f.read()
    return json.loads(data)
