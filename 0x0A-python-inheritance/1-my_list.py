#!/usr/bin/python3
""" 1-my_list module

Contains a class MyList that inherits from list
"""


class MyList(list):
    """ Inherits from list

    Prints a sorted list with print_sorted
    """

    def __init__(self):
        """Initializes the class variables

        Only calls super()
        """

        super().__init__(self)

    def print_sorted(self):
        """prints a sorted list

        Assuming they are all integers
        """

        print(sorted(self))
