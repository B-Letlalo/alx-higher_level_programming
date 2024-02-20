#!/usr/bin/python3

def max_integer(my_list=[]):
    temp = my_list[0]
    if (len(my_list) == 0):
            return None
    else:
        for integers in my_list:
            if (integers > temp):
                temp = integers
            else:
                temp = temp
    return (temp)
