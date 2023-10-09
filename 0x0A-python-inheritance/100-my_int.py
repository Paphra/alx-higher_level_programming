#!/usr/bin/python3
"""100-my_int module

Contains a rebel int class
"""


class MyInt(int):
    """A rebel int class
    """

    def __eq__(self, other):
        """inverting equals (==)
        """

        if isinstance(other, int):
            return self is other
        return False

    def __ne__(self, other):
        """inverting the not equal (!=)
        """

        if isinstance(other, int):
            return self is not other
        return False
