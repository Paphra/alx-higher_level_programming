#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    if len(matrix) > 0:
        for m_item in matrix:
            i = 0
            for elem in m_item:
                end = ''
                if i < len(m_item) - 1:
                    end = ' '
                print("{:d}".format(elem), end=end)
                i += 1
            print()
    else:
        print()
