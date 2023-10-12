#!/usr/bin/python3
"""4-from_json_string module

Contains a function that returns rep by a JSON string
"""

import json


def from_json_string(my_str):
    """Returns an Obj repr by a JSON string
    """

    return json.loads(my_str)
