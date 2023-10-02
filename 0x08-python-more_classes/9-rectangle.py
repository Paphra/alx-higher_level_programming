#!/usr/bin/python3
"""
9-rectangle module

Contains a class Rectangle that defines a rectangle with dimensions
"""


class Rectangle:
    """
    A class that defines a rectangle

    Attr:
        number_of_instances (int): default 0, public
        print_symbol (any): default #, public
        width (int): default 0, private with getter, setter
        height (int): default 0, private witg getter, setter

    Methods:
        __init__(): for initialization
        __str__(): for a string representation
        __repr__(): returns string representation for recreation
        __del__(): detects deletion and says bye

        area(): returns the area of the rectangle
        perimeter(): returns the perimeter of rectangle,
            0 if one or all dimensions = 0

        bigger_or_equal(): static method for comparison
        square(): class method for returning a rectangle instance
    """

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
        Initializes the dimensions of the rectangle
        """

        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    def __str__(self):
        """
        Returns a printable string (rectangle with #)
        """

        rect = ""
        if self.__width == 0 or self.__height == 0:
            return rect
        for i in range(self.__height):
            for j in range(self.__width):
                rect += '{}'.format(self.print_symbol)
            if i < self.__height - 1:
                rect += '\n'

        return rect

    def __repr__(self):
        """
        Returns a canonical string of the class for recreation
        """

        return "Rectangle({:d}, {:d})".format(
            self.__width, self.__height
        )

    def __del__(self):
        """
        Displays a message on class deletion
        """

        Rectangle.number_of_instances -= 1
        print('Bye rectangle...')

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

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
        Compares and returns the rectangle instance that is bigger

        Args:
            rect_1 (Rectangle): first rectangle instance
            rect_2 (Rectangle): second rectangle instance
        """

        if not isinstance(rect_1, Rectangle):
            raise TypeError('rect_1 must be an instance of Rectangle')
        if not isinstance(rect_2, Rectangle):
            raise TypeError('rect_2 must be an instance of Rectangle')
        if rect_1.area() < rect_2.area():
            return rect_2
        return rect_1

    @classmethod
    def square(cls, size=0):
        """
        Returns a Rectangle instance with width = height = size

        Args:
            size (int): the size of the rectangle
        """

        return cls(size, size)
