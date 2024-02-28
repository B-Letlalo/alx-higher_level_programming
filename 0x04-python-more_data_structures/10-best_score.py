#!/usr/bin/python3

def best_score(a_dictionary):
    highest_value = float('-inf')
    highest_key = None
    if not a_dictionary:
        return None
    else:
        for key, values in a_dictionary.items():
            if (values > highest_value):
                highest_value = values
                highest_key = key
        return (highest_key)
