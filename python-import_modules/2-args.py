#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    num_args = len(sys.argv)
    if num_args <= 1:
        print("{} arguments.".format(num_args - 1))
    elif num_args == 2:
        print("{} arguments.".format(num_args - 1))
    else:
        print("{} arguments.".format(num_args - 1))
    for x in range(1, num_args):
        print("{}: {}".format(x, sys.argv[x]))
