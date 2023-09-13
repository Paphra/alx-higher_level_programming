#!/usr/bin/python3
def weight_average(my_list=[]):
    total_keys = 0
    total = 0
    if len(my_list) == 0:
        return 0
    for tup in my_list:
        total += tup[0] * tup[1]
        total_keys += tup[1]
    avg = total / total_keys
    return avg
