#!/usr/bin/python3
"""base module

Contains the Base class for all other classes
"""


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
