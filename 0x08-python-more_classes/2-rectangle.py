#!/usr/bin/python3
"""
2-rectangle module

Contains a class Rectangle that defines a rectangle with dimensions
"""


class Rectangle:
    """
    A class that defines a rectangle

    Attr:
        width (int): default 0, private with getter, setter
        height (int): default 0, private witg getter, setter
    Methods:
        area(): returns the area of the rectangle
        perimeter(): returns the perimeter of rectangle,
            0 if one or all dimensions = 0
    """

    def __init__(self, width=0, height=0):
        """
        Initializes the dimensions of the rectangle
        """

        self.width = width
        self.height = height

    @property
    def width(self):
        """
        Returns the width of the rectangle
        """

        return self.__width

    @width.setter
    def width(self, value):
        """
        Sets the width of the rectangle

        Args:
            value (int): must be an integer >= 0
        """

        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """
        Returns the height of the rectangle
        """

        return self.__height

    @height.setter
    def height(self, value):
        """
        Sets the width of the rectangle

        Args:
            value (int): must be an integer >= 0
        """

        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self):
        """
        Returns the area of a rectangle
        """

        return self.__width * self.__height

    def perimeter(self):
        """
        Returns the perimeter of the rectangle
            0 if with=0, or height=0, or both=0
        """

        if self.__width == 0 or self.__height == 0:
            return 0
        return self.__width * 2 + self.__height * 2
