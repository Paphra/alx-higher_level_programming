#!/usr/bin/python3
"""11-square module

Contains a BaseGeometry class
and the Rctangle class
and the Square class
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

        self.integer_validator('width', width)
        self.integer_validator('height', height)

        self.__width = width
        self.__height = height

    def area(self):
        """Returns the area
        """

        return self.__width * self.__height

    def __str__(self):
        """For printing
        """

        return "[Rectangle] {}/{}".format(self.__width, self.__height)


class Square(Rectangle):
    """Defines the size and the area
    """

    def __init__(self, size):
        """Initializes the square
        """

        self.integer_validator("size", size)

        self.__size = size

        super().__init__(size, size)

    def area(self):
        """Overrides the area and returns area of square
        """

        return self.__size**2

    def __str__(self):
        """Returns a printable string
        """

        return "[Square] {}/{}".format(self.__size, self.__size)
