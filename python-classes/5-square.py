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

    @property
    def size(self):
        """returns the size"""
        return self.__size

    @size.setter
    def size(self, value):
        """sets the value of size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """returns the area"""
        return self.__size ** 2

    def my_print(self):
        """print the square"""
        for y in range(0, self.__size):
            if y == 0 or y == self.__size - 1:
                print("#" * self.__size)
            else:
                for x in range(0, self.__size):
                    if x == 0 or x == self.__size - 1:
                        print("#", end="")
                    else:
                        print(" ", end="")
        if self.__size == 0:
            print()
