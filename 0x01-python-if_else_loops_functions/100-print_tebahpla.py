#!/usr/bin/python3
idx = 0
for letter in "abcdefghijklmnopqrstuvwxyz"[::-1]:
    print(
            "{}".format(
                letter if idx % 2 == 0 else
                "ABCDEFGHIJKLMNOPQRSTUVWXYZ"[::-1][idx]),
            end=""
    )
    idx += 1
