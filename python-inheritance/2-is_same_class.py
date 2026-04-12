#!/usr/bin/python3
"""defines a function that check if an object is same class"""


def is_same_class(obj, a_class):
    """checks if an object is same class"""
    if type(obj) is a_class:
        return True
    return False
