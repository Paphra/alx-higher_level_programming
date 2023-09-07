#!/usr/bin/python3

if __name__ == "__main__":
    from sys import argv
    num = len(argv)

    if num > 1:
        ends = 's:'
        if num == 2:
            ends = ':'
        print("{} argument{}".format(num - 1, ends))
        for i in range(1, num):
            print("{}: {}".format(i, argv[i]))
    else:
        print("{} arguments.".format(num - 1))
