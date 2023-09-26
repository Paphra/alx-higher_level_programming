#!/usr/bin/python3
"""1-square module

Creating the Square classs
Todo:
    * Add a private instance attribute: size

"""


class Square:
    """Class Square

    Square class
    Args: None
    Attributes:
        __size (str): the size of the square

    """

    def __init__(self, size=0):
        """__init__ method.

        Initializing the class attributes
        Args:
            size: the size of the square

        """

        self.__size = size
