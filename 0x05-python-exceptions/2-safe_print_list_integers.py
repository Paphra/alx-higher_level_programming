#!/usr/bin/python3
def safe_print_list_integers(my_list=[], x=0):
    i = 0
    printed = 0
    while (i < x):
        item = my_list[i]
        try:
            print("{:d}".format(item), end='')
        except Exception:
            i += 1
            continue
        else:
            printed += 1
        i += 1
    print()
    return printed
