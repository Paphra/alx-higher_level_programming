#!/usr/bin/python3
"""103-magic_class module
Contains a magic class
"""


class MagicClass:
    """class MagicClass
    Calculates the area and circumfrence of a circle
    """

    def __init__(self, radius=0):
        """__init__ method
        Initialize variables
        Args:
            radius (int, float): integer or float radius
        Actions:
            * check type to be int or float
            * initialize __radius
        """

        if type(radius) is not int or type(radius) is not float:
            raise TypeError('radius must be a number')
        self.__radius = radius

    def area(self):
        """area method
        Returns the area of a circle
        """

        return (self.__radius**2) * math.pi

    def circumference(self):
        """circumference method
        Returns the circumference of ths circle
        """

        return 2 * math.pi * self.__radius
