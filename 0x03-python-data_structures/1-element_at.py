#!/usr/bin/python3
def element_at(my_list, idx):
    count = len(my_list)
    if idx < 0 and idx >= count:
        return None
    return my_list[idx]
