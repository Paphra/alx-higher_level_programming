#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    count = len(my_list)
    lcopy = my_list[:]
    if idx > 0 and idx < count:
        lcopy[idx] = element
    return lcopy
