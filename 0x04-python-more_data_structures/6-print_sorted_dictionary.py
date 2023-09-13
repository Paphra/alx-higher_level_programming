#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    keys = a_dictionary.keys()
    keys = sorted(keys)
    for key in keys:
        print("{}: {}".format(key, a_dictionary.get(key)))
