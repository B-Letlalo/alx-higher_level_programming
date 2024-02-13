#!/usr/bin/python3
import sys
i = 1
counter = 1

if __name__ == "__main__":
    num_args = len(sys.argv)
    if (num_args == 1):
        print("0 arguments.")
    elif (num_args == 2):
        print(f"1 argument:")
        print(f"1: {sys.argv[i]}")
    else:
        # Number of arguments here excludes the script name
        print("{} arguments:".format(num_args - 1))
        for i in range(1, num_args):
            print("{}: {}".format(i, sys.argv[i]))
