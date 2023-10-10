#!/usr/bin/python3
"""1-write_file module

Contains a function that writes to a file
"""


def write_file(filename="", text=""):
    """Writes some given text to the file
    
    Args:
        filename (str): string file name
        text (str): the text to write
    """

    with open(filename, 'w', encoding='utf-8') as f:
        return f.write(text)
