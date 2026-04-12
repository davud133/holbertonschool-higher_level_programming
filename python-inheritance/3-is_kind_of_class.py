#!/usr/bin/python3
"""defines a function to check if an object is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """check if an object is an instance of a class"""
    if isinstance(obj, a_class):
        return True
    return False
