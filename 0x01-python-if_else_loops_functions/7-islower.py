#!/usr/bin/python3
def islower(c):
    for letter in 'abcdefghijklmnopqrstuvwxyz':
        if ord(c) is ord(letter):
            return True
    return False
