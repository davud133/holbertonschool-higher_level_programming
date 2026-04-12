#!/usr/bin/python3
"""defines a function that checks if an object is instance of a an another class that inherited from another class"""


def inherits_from(obj, a_class):
    """checks if an object is instance of class that inherited from another class"""
    if isinstance(obj, a_class) and len(a_class.__mro__) > 2:
        return True
    return False
