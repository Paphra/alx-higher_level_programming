#!/usr/bin/python3
def add_tuple(tuple_a=(), tuple_b=()):
    sum0 = 0
    sum1 = 0

    la = len(tuple_a)
    lb = len(tuple_b)

    if la > 0:
        sum0 += tuple_a[0]
    if la > 1:
        sum1 += tuple_a[1]
    if lb > 0:
        sum0 += tuple_b[0]
    if lb > 1:
        sum1 += tuple_b[1]

    return (sum0, sum1)
