#!/usr/bin/python3
def add_integer(a, b=98):
    if not (type(a) is in [int, float] and type(b) is in [int, float]):
        raise typeError("a must be an integer or b must be an integer")
    return int(a) + int(b)
