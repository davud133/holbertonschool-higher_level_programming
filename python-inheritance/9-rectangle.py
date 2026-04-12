#!/usr/bin/python3
"""defines a Rectangle class inherited from BaseGeometry"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """defines a Rectangle class inherited from BaseGeometry"""
    def __init__(self, width, height):
        """initilizes the width and height"""
        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        return self.__width * self.__height

    def __str__(self):
        width = self.__width
        height = self.__height
        return "[Rectangle] {width}/{height}".format(width=width, height=height)
