#!/usr/bin/python3
import sys
i = 1
counter = 1

num_args = len(sys.argv)
if (__name__ == "__main__"):
    if (num_args == 1):
        print(f"0 arguments")
    else:
        # Number of arguments here excludes the script name
        print(f"{num_args - 1} arguments:")
        for i in range(1, num_args):
            print(f"{i}: {sys.argv[i]}")
