#!/usr/bin/python3
def pow(a, b):
    tmp = a
    for i in range (1, b):
        a = a * tmp
    return a
