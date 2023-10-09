#!/usr/bin/python3
"""7-base_geometry module

Contains a BaseGeometry class
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

        if type(value) is not int:
            raise TypeError('{} must be an integer'.format(name))
        if value <= 0:
            raise ValueError('{} must be greater than 0'.format(name))
