#!/usr/bin/python3
def uniq_add(my_list=[]):
    tmp = []
    total = 0
    for x in my_list:
        if x not in tmp:
            total += x
            tmp.append(x)
    return total
