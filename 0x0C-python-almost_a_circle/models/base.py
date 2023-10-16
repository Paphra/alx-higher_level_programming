#!/usr/bin/python3
"""base module

Contains the Base class for all other classes
"""


import json


class Base:
    """The Base class for all other classes
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialize all variables

        Args:
            id (int): an integer ID
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a json representaion of the list_dictionaries

        Args:
            list_dictionaries (list): can be None or empty
        """
        
        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"
        json_string = json.dumps(list_dictionaries)
        return json_string
