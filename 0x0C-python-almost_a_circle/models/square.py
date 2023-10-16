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

    @property
    def size(self):
        """Returns the size of the square, based on the Rectangle width
        """

        return self.width

    @size.setter
    def size(self, value):
        """Sets the size of the Square

        Args:
            value (int): a required integer for size
                sets it to width then height
        """

        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Update the attributes of the square class
        """

        cargs = len(args)
        if cargs > 0:
            attrs = ['id', 'size', 'x', 'y']
            for i in range(cargs):
                setattr(self, attrs[i], args[i])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

    def to_dictionary(self):
        """Returns the dict rep of the square instance
        """

        dic = {
            'id': self.id,
            'size': self.size,
            'x': self.x,
            'y': self.y,
        }

        return dic
