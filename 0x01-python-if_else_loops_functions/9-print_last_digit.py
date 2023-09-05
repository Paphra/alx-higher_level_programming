#!/usr/bin/python3
def print_last_digit(number):
    _abs = number
    if number < 0:
        _abs *= -1
    last = _abs % 10
    print("{}".format(last), end="")
    return last
