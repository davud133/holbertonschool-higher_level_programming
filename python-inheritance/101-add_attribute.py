#!/usr/bin/python3
"""defines a function to add attribute to a class if possible"""


def add_attribute(obj, name, value):
    """checks if adding is possible"""
    if hasattr(obj, "__dict__"):
        setattr(obj, name, value)
    else:
        raise TypeError("can't add new attribute")
