#!/usr/bin/python3
def pow(a, b):
    int tmp = a
    for i in range (0, b):
        a = a * tmp
    return a
