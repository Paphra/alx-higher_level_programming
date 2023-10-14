#!/usr/bin/python3
"""rectangle module

Contains a class Rectangle that inherits from Base
"""


from .base import Base


class Rectangle(Base):
    """Rectangle class for definition of a rectangle
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializing all member attributes
        """

        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Returns the width of a rectangle
        """

        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of a rectangle

        Args:
            value (int): an integer of the width
        TODO:
            validate the input: an integer > 0
        """

        if type(value) is not int:
            raise TypeError('width must be an integer')
        if value <= 0:
            raise ValueError('width must be > 0')
        self.__width = value

    @property
    def height(self):
        """Returns the height of a rectangle
        """

        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of a rectangle

        Args:
            value (int): an integer value representing the height
        TODO:
            validate the value: an integer > 0
        """

        if type(value) is not int:
            raise TypeError('height must be an integer')
        if value <= 0:
            raise ValueError('height must be > 0')

        self.__height = value

    @property
    def x(self):
        """Returns the x value of the rectangle
        """

        return self.__x

    @x.setter
    def x(self, value):
        """Sets the x value of the rect

        Args:
            value (int): the integer rep of x
        TODO:
            validate value: an integer >= 0
        """

        if type(value) is not int:
            raise TypeError('x must be an integer')
        if value < 0:
            raise ValueError('x must be >= 0')
        self.__x = value

    @property
    def y(self):
        """returns the y value of the rect
        """

        return self.__y

    @y.setter
    def y(self, value):
        """Sets the y value of the rect

        Args:
            value (int): the integer rep of y
        TODO:
            validate the value: an integer >= 0
        """

        if type(value) is not int:
            raise TypeError('y must be an integer')
        if value < 0:
            raise ValueError('y must be >= 0')
        self.__y = value

    def area(self):
        """Returns the area value of the Rectangle instance
        """

        return self.__width * self.__height

    def display(self):
        """Display a rectangle using #
        """

        for i in range(self.__height):
            for j in range(self.__width):
                print('#', end='')
            print()

    def __str__(self):
        """Returns a string representation of the Rectangle
        """

        rep = "[Rectangle] ({id}) {x}/{y} - {width}/{height}".format(
                id=self.id, x=self.__x, y=self.__y, width=self.__width,
                height=self.__height)
        return rep
