#!/usr/bin/python3
def roman_to_int(roman_string):
    my_d = {
        "I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000
    }
    total = 0
    if type(roman_string) is not str or roman_string is None:
        return total
    prev = ''
    for i in roman_string:
        total += my_d.get(i)
        if prev == 'I' and i != 'I':
            total -= 2
        prev = i
    return total
