#!/usr/bin/python3
"""
5-text_indentation module

Contains a function that prints a text with 2 new lines
after each of these characters: ., ? and :
"""


def text_indentation(text):
    """
    Prints a text with two new lines after the given chars
    """

    if type(text) is not str:
        raise TypeError('text must be a string')

    lines = []
    for delim in ['.', '?', ':']:
        text = text.replace(delim, delim + '\n')
    lines = text.split('\n')

    for i in range(len(lines)):
        print(lines[i].strip(), end='')
        if i < len(lines) - 1:
            print('\n')
