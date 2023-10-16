#!/usr/bin/python3
"""square module

Contains the class Square that inherits from Rectangle
"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Defines a Square class rep. a square dimension
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initializes all the attributes of the class

        Args:
            size: a required integer
            x: the x-position on the grid (int)
            y: the y-position on the grid (int)
        """

        super().__init__(size, size, x, y, id)

    def __str__(self):
        """Returns a string rep of the class
        """

        rep = '[Square] ({id}) {x}/{y} - {size}'.format(
                id=self.id, x=self.x, y=self.y,
                size=self.width)
        return rep
