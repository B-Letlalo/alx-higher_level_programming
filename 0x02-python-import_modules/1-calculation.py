#!/usr/bin/python3
from calculator_1 import add, sub, mul, div

a = 10
b = 5

if (__name__ == "__main__"):
    addition = add(a, b)
    print(f"{a} + {b} = {addition}")
    subtraction = sub(a, b)
    print(f"{a} - {b} = {subtraction}")
    multiplication = mul(a, b)
    print(f"{a} * {b} = {multiplication}")
    division = div(a, b)
    print(f"{a} / {b} = {division}")
