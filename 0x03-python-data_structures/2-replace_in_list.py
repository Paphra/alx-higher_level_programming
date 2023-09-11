#!/usr/bin/python3
def replace_in_list(my_list, idx, element):
    lcp = my_list[:]
    if idx < 0 or idx >= len(my_list):
        return my_list
    lcp[idx] = element
    return lcp
