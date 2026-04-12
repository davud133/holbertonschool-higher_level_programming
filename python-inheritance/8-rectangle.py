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
