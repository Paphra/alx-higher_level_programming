#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    tmp = {}
    for k, v in a_dictionary.items():
        tmp[k] = v
    for k, v in tmp.items():
        if v == value:
            a_dictionary.pop(k)
    return a_dictionary
