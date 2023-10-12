#!/usr/bin/python3
"""100-append_after module

Contains a function that appends a text to a file
"""


def append_after(filename="", search_string="", new_string=""):
    """Appends a line of text to a file

    This is done every after a line that contains a specific string
    Args:
        filename (str): the file name
        search_string (str): the string to search for
        new_string (str): the line of text to insert
    Returns: None
    """

    original_lines = []
    with open(filename, 'r') as f:
        original_lines = f.readlines()

    new_lines = []
    for line in original_lines:
        new_lines.append(line)
        if search_string in line:
            new_lines.append(new_string)

    with open(filename, 'w') as f:
        f.writelines(new_lines)
