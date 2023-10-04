#!/usr/bin/python3
"""Locked class module
"""


class LockedClass:
    """Locked class
    """

    def __setattr__(self, name, value):
        """ set attribute method

        Only allow first_name
        """

        if name == 'first_name' and hasattr(self, name):
            super().__setattr__(name, value)
        else:
            raise AttributeError(
                "'{}' object has no attribute '{}'".format(
                    type(self).__name__, name
                )
            )
