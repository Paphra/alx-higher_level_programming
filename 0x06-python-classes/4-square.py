#!/usr/bin/python3
"""4-square module

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
    Todo:
        *add a public instance method area
        *add public setter and getter methods for size
    """

    def __init__(self, size=0):
        """__init__ method.

        Initializing the class attributes
        Args:
            size: the size of the square
        Actions:
            if type is not int: raise TypeError
            if size < 0: raise ValueError

        """

        self.size = size

    def area(self):
        """area method.

        Returns the current square area

        """

        result = self.__size * self.__size

        return (result)

    @property
    def size(self):
        """size method

        Get the size of the square from the private variable

        """

        return self.__size

    @size.setter
    def size(self, value=0):
        """size: setting

        Setting the size private attribute a given value
        Args:
            value: the value of the new size

        """

        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value
