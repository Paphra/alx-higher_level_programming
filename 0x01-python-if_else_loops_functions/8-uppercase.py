#!/usr/bin/python3
def uppercase(str):
    uppers = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    lowers = "abcdefghijklmnopqrstuvwxyz"
    for char in str:
        if char in lowers:
            char = uppers[lowers.find(char)]
        print("{}".format(char), end="")
    print()
