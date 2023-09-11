#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    checks = []
    for i in my_list:
        if i % 2 == 0:
            checks.append(True)
        else:
            checks.append(False)
    return checks
