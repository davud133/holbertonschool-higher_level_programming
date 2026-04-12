#!/usr/bin/python3
"""defines a Square class inherited from Rectangle class"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """defines a Square class"""
    def __init__(self, size):
        """initilizes the size variable"""
        super().integer_validator("size", size)
        self.__size = size

    def area(self):
        """return the area of Square"""
        return self.__size ** 2

    def __str__(self):
        return "[Square] {w}/{h}".format(w=self.__size, h=self.__size)
