#!/usr/bin/python3
"""6-square module

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
        __position (tuple): of two positive integers
    Todo:
        *add a public instance method area
        *add public setter and getter methods for size
        *add public instance method my_print

    """

    def __init__(self, size=0, position=(0, 0)):
        """__init__ method.

        Initializing the class attributes
        Args:
            size: the size of the square
            position: tuple of 2 positives
        Actions:
            if type is not int: raise TypeError
            if size < 0: raise ValueError
            if position is not as described, TypeError

        """

        self.size = size
        self.position = position

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
    def size(self, value):
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

    @property
    def position(self):
        """position: getter

        Get the current position
        """

        return self.__position

    @position.setter
    def position(self, value):
        """position: setter

        Set the current position to a value
        """
        if type(value) is not tuple or len(value) != 2:
            raise TypeError(
                'position must be a tuple of 2 positive integers')
        if type(value[0]) is not int or type(value[1]) is not int:
            raise TypeError(
                'position must be a tuple of 2 positive integers')
        if value[0] < 0 or value[1] < 0:
            raise TypeError(
                'position must be a tuple of 2 positive integers')

        self.__position = value

    def my_print(self):
        """my_print method

        Prints in sdtout the square with the character #
        Actions:
            If the size if 0, print empty line

        """

        if (self.__size == 0):
            print()
        else:
            if self.__position[1] > 0:
                print()
            for i in range(self.__size):
                for k in range(self.__position[0]):
                    print(' ', end='')
                for j in range(self.__size):
                    print('#', end='')
                print()
