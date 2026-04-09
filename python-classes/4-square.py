#!/usr/bin/python3
"""defines a class square"""


class Square:
    """defines a square class"""
    
    def __init__(self, size=0):
        """initilizes the size variable"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
    def size(self):
        """returns the size"""
        return self.__size
    def size(self, value):
        """sets the value of size"""
        if type(value) is not int:
            raise TypeError("value must be an integer")
        if value < 0:
            raise ValueError("Value must be >= 0")
        self.__size = value
    def area(self):
        """returns the area"""
        return self.__size ** 2
