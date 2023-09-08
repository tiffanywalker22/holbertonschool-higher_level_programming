#!/usr/bin/python3
from sys import argv

if __name__ == "__main__":
    num_args = len(argv)
    if num_args == 1:
        print(("0 arguments."))
    else:
         print("{} {}:".format(args - 1, "argument" if num_args == 2 else "arguments"))
    for x in range(1, num_args):
        print("{}: {}".format(x, sys.argv[x]))
