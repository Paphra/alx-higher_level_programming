#!/usr/bin/python3
"""2-square module

Creating the Square classs
Todo:
    * Add a private instance attribute: size

"""


class Square:
    """Class Square

    Square class
    Args: None
    Attributes:
        __size (int): the size of the square

    """

    __size = 0

    def __init__(self, size=0):
        """__init__ method.

        Initializing the class attributes
        Args:
            size: the size of the square
        Actions:
            if type is not int: raise TypeError
            if size < 0: raise ValueError

        """

        if type(size) is not int:
            raise TypeError('size must be an integer')
        if size < 0:
            raise ValueError('size must be >= 0')
        self.__size = size
