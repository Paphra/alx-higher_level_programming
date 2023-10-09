#!/usr/bin/python3
"""8-rectangle module

Contains a BaseGeometry class
and the Rctangle class
"""


class BaseGeometry:
    """Defines the following instance methods

    area(): raises an exception
    integer_validator(): validates an integer
    """

    def area(self):
        """Raises an exception
        """

        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Validates an integer
        """

        if not isinstance(value,  int) or type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))


class Rectangle(BaseGeometry):
    """Defines the rectangle geometry
    """

    def __init__(self, width, height):
        """Initialization ofthe given values
        """

        BaseGeometry.integer_validator(self, 'width', width)
        BaseGeometry.integer_validator(self, 'height', height)

        self.__width = width
        self.__height = height
