#!/usr/bin/python3
"""defines a basegeometry class"""


class BaseGeometry:
    """defines a BaseGeometry class"""
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        if not isinstance(value, int):
            raise TypeError("{name} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{name} must be greater than 0".format(name))
