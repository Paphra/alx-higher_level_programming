#!/usr/bin/python3
def remove_char_at(str, n):
    str_cpy = ""
    idx = 0
    for char in str:
        if idx != n:
            str_cpy += char
        idx += 1
    return str_cpy
