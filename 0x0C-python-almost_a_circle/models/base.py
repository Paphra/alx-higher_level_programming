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

    @classmethod
    def save_to_file(cls, list_objs):
        """Save the given list objects to file

        Args:
            cls: the class that is calling this function
            list_objs: the list of objects being saved
        """

        f_name = '{}.json'.format(cls.__name__)
        list_dict = [obj.to_dictionary() for obj in list_objs]
        json_str = Base.to_json_string(list_dict)
        with open(f_name, 'w') as f:
            f.write(json_str)

    @staticmethod
    def from_json_string(json_string):
        """Convert from json string to the correct data type

        Args:
            json_string: the string to convert
        """

        if type(json_string) is not str and json_string is not None:
            raise TypeError

        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)
