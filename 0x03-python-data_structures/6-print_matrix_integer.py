#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    count = len(matrix)
    if count > 0:
        for arr in matrix:
            citems = len(arr)
            i = 0
            for item in arr:
                end = ''
                if i < citems - 1:
                    end = ' '
                print("{num:d}".format(num=item), end=end)
                i += 1
            print()
    else:
        print()
