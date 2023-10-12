#!/usr/bin/python3
"""5-save_to_json_file module

Cotains a function that writes a JSON repr obj to a file
"""


import json


def save_to_json_file(my_obj, filename):
    """Writes an Obj to a text file using JSON repr
    """

    with open(filename, 'w') as f:
        f.write(json.dumps(my_obj))
