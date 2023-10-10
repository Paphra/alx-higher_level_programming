#!/usr/bin/python3
"""0-read_file module

Contains a function that reads a file
"""


def read_file(filename=""):
    """Reads a given file
    """

    with open(filename, 'r', encoding='utf-8') as f:
        print(f.read(), end='')
