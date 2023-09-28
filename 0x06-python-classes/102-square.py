#!/usr/bin/python3
"""102-square module

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

    def __eq__(self, other):
        """__eq__ method
        Compares whether this class is equal to another
        Args:
            other (Square): the other class
        Returns: bool
        """

        if isinstance(other, Square):
            return self.area() == other.area()
        return False

    def __ne__(self, other):
        """__ne__ method
        Compares whether this class is not equal to another
        Args:
            other (Square): the other class
        Returns: bool
        """

        if isinstance(other, Square):
            return self.area() != other.area()
        return False

    def __gt__(self, other):
        """__gt__ method
        Compares whether this class is greater than another
        Args:
            other (Square): the other class
        Returns: bool
        """

        if isinstance(other, Square):
            return self.area() > other.area()
        return False

    def __ge__(self, other):
        """__ge__ method
        Compares whether this class is greater or equal to another
        Args:
            other (Square): the other class
        Returns: bool
        """

        if isinstance(other, Square):
            return self.area() >= other.area()
        return False

    def __lt__(self, other):
        """__lt__ method
        Compares whether this class is less than another
        Args:
            other (Square): the other class
        Returns: bool
        """

        if isinstance(other, Square):
            return self.area() < other.area()
        return False

    def __le__(self, other):
        """__le__ method
        Compares whether this class is less or equal to another
        Args:
            other (Square): the other class
        Returns: bool
        """

        if isinstance(other, Square):
            return self.area() <= other.area()
        return False

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
