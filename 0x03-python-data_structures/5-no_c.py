#!/usr/bin/python3

def no_c(my_string):
    new_string = ""
    for letters in my_string:
        if letters not in "Cc":
            new_string += letters
    return (new_string)
