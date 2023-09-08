#!/usr/bin/env python3
def no_c(my_string):
    length = len(my_string)
    scopy = ''
    for char in my_string:
        if char not in ['c', 'C']:
            scopy += char
    return scopy
