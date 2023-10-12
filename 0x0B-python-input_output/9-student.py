#!/usr/bin/python3
"""9-student module

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

    def to_json(self):
        """Returns a dict repr. of a student instance
        """

        return self.__dict__
