#!/usr/bin/python3
def pow(a, b):
    if b == 0:
        return 1
    if b < 0:
        return 1 / pow(a, -b)

    if b % 2 == 0:
        half = pow(a, b // 2)
        return half * half
    else:
        return a * pow(a, b - 1)
