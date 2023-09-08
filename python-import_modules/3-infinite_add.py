#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num_args = len(argv)
    sum = 0
    if num_args == 1:
        print("0")
        elif num_args == 2
            print("{}".format(argv[1]))
        else:
            for x in range(1, num_args):
                sum += int(argv[x])
            print("{}".format(sum))
