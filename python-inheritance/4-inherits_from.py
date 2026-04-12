#!/usr/bin/python3
"""
defines a function that checks if
an object is instance of a an
another class that inherited from another class
"""


def inherits_from(obj, a_class):
    """
    checks if an object is instance
    of class that inherited from another class
    """
    return isinstance(obj, a_class) and type(obj) is not  a_class
