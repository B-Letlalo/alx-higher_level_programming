#!/usr/bin/python3

def print_sorted_dictionary(a_dictionary):
    sorted_list = sorted(a_dictionary.items())
    for key, value in sorted_list:
        print(f"{key}: {value}")
