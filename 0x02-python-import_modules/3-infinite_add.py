#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv

    num = len(argv)
    total = 0
    for i in range(1, num):
        arg = int(argv[i])
        total += arg
    print("{}".format(total))
