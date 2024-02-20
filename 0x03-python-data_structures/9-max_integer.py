#!/usr/bin/python3

def max_integer(my_list=[]):
    ll = len(my_list)
    if (ll == 0):
        return None
    else:
        temp = my_list[0]
        for integers in my_list:
            if (integers > temp):
                temp = integers
            else:
                temp = temp
        return (temp)
