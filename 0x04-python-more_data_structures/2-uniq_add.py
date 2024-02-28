#!/usr/bin/python3

def uniq_add(my_list=[]):
    sum = 0
    unique_set = set(my_list)
    for items in unique_set:
        sum += items
    return (sum)
