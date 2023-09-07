#!/usr/bin/python3
import sys

def print_arguments(argv):
    num_args = len(argv)
    if num_args == 0:
        print("0 arguments.")
        print(".")
    elif num_args == 1:
        print("1 argument:")
        print("1:", argv[0])
    else:
        print(str(num_args) + "arguments:")
        position = 1
        for arg in argv:
            print(str(position) + ":", arg)
            position += 1
if __name__ == "__main__":
    print_arguments(sys.argv[1:])
