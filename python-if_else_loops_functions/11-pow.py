#!/usr/bin/python3
def pow(a, b):
    tmp = a
    if b < 0:
        for i in range(1, b, -1):
            a = a / tmp
    elif b > 0:
        for i in range(1, b):
            a = a * tmp
    return a
