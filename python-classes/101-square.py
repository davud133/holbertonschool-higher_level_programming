#!/usr/bin/python3
"""defines a class square"""


class Square:
    """defines a square class"""

    def __init__(self, size=0, position=(0, 0)):
        """initilizes the size and position variable"""
        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
        if not (type(position) is tuple and
                len(position) == 2 and
                type(position[0]) is int and
                type(position[1]) is int and
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
        if not (type(value) is tuple and
                len(value) == 2 and
                type(value[0]) is int and
                type(value[1]) is int and
                value[0] >= 0 and value[1] >= 0):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """returns the area"""
        return self.__size ** 2

    def my_print(self):
        """print the square"""
        if self.__size == 0:
            print()
        else:
            for py in range(0, self.__position[1]):
                print()
            for y in range(0, self.__size):
                for px in range(0, self.__position[0]):
                    print(" ", end="")
                print("#" * self.__size)

    def __str__(self):
        ss = ""
        if self.__size == 0:
            return ss
        else:
            for py in range(0, self.__position[1]):
                ss = ss + "\n"
            for y in range(0, self.__size):
                for px in range(0, self.__position[0]):
                    ss = ss + " "
                ss + "#" * self.size + ("\n" if y != self.size - 1 else "")
        return ss
