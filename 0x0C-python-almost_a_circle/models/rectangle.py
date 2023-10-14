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
        """

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
        """

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
        """

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
        """

        self.__y = value
