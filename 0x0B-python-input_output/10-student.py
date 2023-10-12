#!/usr/bin/python3
"""10-student module

Contains a class Student
"""


class Student:
    """Describes a student instance
    """

    def __init__(self, first_name, last_name, age):
        """Initializing the instance attributes
        """

        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Returns a dict repr. of a student instance
        """

        dic = self.__dict__
        result = dict()
        if attrs is not None:
            for att in attrs:
                if att in dic.keys():
                    result[att] = dic.get(att)
        else:
            result = dic
        return result
