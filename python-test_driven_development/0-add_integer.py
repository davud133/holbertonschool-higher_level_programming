#!/usr/bin/python3
def add_integer(a, b=98):
    """
        Returns the sum of 2 numbers
    """
    if not type(a) in [int, float]:
        raise TypeError("a must be an integer")
    if not type(a) in [int, float]:
        raise typeError("b must be an integer")
    return int(a) + int(b)
