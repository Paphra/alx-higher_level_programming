#!/usr/bin/python3
def element_at(my_list, idx):
    count = len(my_list)
    if idx < 0:
        return None
    i = 0
    for num in my_list:
        if i == idx:
            return num
        i += 1
    return None
