#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    try:
        count = 0
        while (count < x):
            print("{}".format(my_list[count]), end='')
            count += 1
    except Exception:
        print()
    else:
        print()
    return (count)
