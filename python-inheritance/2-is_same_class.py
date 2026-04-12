#!/usr/bin/python3
"""defines a function that check if an object is an instances of a class"""


def is_same_class(obj, a_class):
    """checks if an object is instance of a class"""
    if isintance(obj, a_class):
        return True
    return False
