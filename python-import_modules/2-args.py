#!/usr/bin/python3
import sys

def print_arguments(argv):
    num_args = len(argv)
    if num_args == 1:
        print("1 arguments.")
        print("1:", argv[0])
    elif num_args > 1:
       print(str(num_args) + " arguments:")
       for i in range(num_args):
            print(str(i + 1) + ":", argv[i])
    else:
        print("0 arguments.")
        print(".")
if __name__ == "__main__":
    print_arguments(sys.argv[1:])
