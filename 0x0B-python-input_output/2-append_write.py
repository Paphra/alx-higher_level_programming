#!/usr/bin/python3
"""2-append_file module

Contains a function that appends a file or
create it if not exist
"""


def append_write(filename="", text=""):
    """Opens a file for appending

    Args:
        filename (str): a tring for filename
        text (str): the string for the text to append
    """

    with open(filename, "a+", encoding='utf-8') as f:
        return f.write(text)
