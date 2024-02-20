#!/usr/bin/python3

def multiple_returns(sentence):
    string_len = len(sentence)
    if (string_len == 0):
        first = None
    else:
        first = sentence[0]
    return (string_len, first)
