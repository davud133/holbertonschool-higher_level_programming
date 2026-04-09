#!/usr/bin/python3
"""defines a class square"""


class Square:
    """defines a square class"""

    def __init__(self, size=0, position=(0,0)):
        """initilizes the size and position variable"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if not (type(position) == tuple and
                len(position) == 2 and
                type(position[0]) == int and
                type(position[1]) == int and
                position[0] >= 0 and position[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = position


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

    @property
    def position(self):
        """returns the position"""
        return self.__position

    @position.setter
    def position(self, value):
        """sets the value of position"""
        if not (type(value) == tuple and
                len(value) == 2 and
                type(value[0]) == int and
                type(value[1]) == int and
                value[0] >= 0 and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        position = value
    def area(self):
        """returns the area"""
        return self.__size ** 2

    def my_print(self):
        """print the square"""
        for px in range(0, position[1]):
            print()
        for py in range(0, position[0]):
            print(" ", end="")
        for y in range(0, self.__size):
            print("#" * self.__size)
        if self.__size == 0:
            print()
