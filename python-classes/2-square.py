#!/usr/bin/python3
"""defines a class about square"""


class Square:
    """defines a class about square"""

    def __init__(self, size=0):
        """initilizes the size variable"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
