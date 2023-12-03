#!/usr/bin/python3
import sys

sum = 0
num_args = len(sys.argv)

if (__name__ == "__main__"):
    for i in range(1, num_args):
        sum = sum + int(sys.argv[i])
    print(sum)
