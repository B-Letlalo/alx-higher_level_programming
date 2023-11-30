#!/usr/bin/python3
for letters in "abcdefghijklmnopqrstuvwxyz":
    if (letters == "q" or letters == "e"):
        continue
    else:
        print(letters, end=' ')
