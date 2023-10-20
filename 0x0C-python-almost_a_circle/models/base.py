#!/usr/bin/python3
"""base module

Contains the Base class for all other classes
"""


import json
import os
import csv


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

        json_str = "[]"
        f_name = '{}.json'.format(cls.__name__)
        if list_objs is not None:
            list_dict = [obj.to_dictionary() for obj in list_objs]
            json_str = Base.to_json_string(list_dict)
        with open(f_name, 'w') as f:
            f.write(json_str)

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Save the given list objects to file

        Args:
            cls: the class that is calling this function
            list_objs: the list of objects being saved
        """

        headers = ['id', 'size', 'x', 'y']
        if cls.__name__ == 'Rectangle':
            headers = ['id', 'width', 'height', 'x', 'y']
        f_name = '{}.csv'.format(cls.__name__)
        with open(f_name, 'w', newline='') as f:
            writer = csv.DictWriter(f, fieldnames=headers)
            writer.writeheader()
            if list_objs is not None:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                for row in list_dict:
                    writer.writerow(row)

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

    @classmethod
    def create(cls, **dictionary):
        """Create an instance from the dictionary

        Args:
            dictionary: a dict of the class attributes
        """

        dummy = None
        if cls.__name__ == 'Square':
            dummy = cls(2)
        elif cls.__name__ == 'Rectangle':
            dummy = cls(3, 2)

        if dummy is not None:
            dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """Load list of json objects from file
        """

        f_name = '{}.json'.format(cls.__name__)
        if os.path.exists(f_name):
            o_list = []
            with open(f_name, 'r') as f:
                contents = f.read()
                json_fstr = cls.from_json_string(contents)
                for jitem in json_fstr:
                    o_list.append(cls.create(**jitem))
            return o_list
        else:
            return []

    @classmethod
    def load_from_file_csv(cls):
        """Load list of json objects from file
        """

        f_name = '{}.csv'.format(cls.__name__)
        if os.path.exists(f_name):
            o_list = []
            with open(f_name, 'r') as f:
                reader = csv.DictReader(f)
                for row in reader:
                    item = {}
                    for k, v in row.items():
                        item[k] = json.loads(v)
                    o_list.append(cls.create(**item))
            return o_list
        else:
            return []

    @staticmethod
    def draw(list_rectangles, list_squares):
        """Draw the shapes using turtle
        """

        pass
