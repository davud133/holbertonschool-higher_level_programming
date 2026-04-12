#!/usr/bin/python3
"""defines duck typing"""


from abc import ABC, abstractmethod
import math

class Shape(ABC):
    """defines Shape class"""
    @abstractmethod
    def area(self):
        """return the area"""
        pass

    @abstractmethod
    def perimeter(self):
        """return the perimeter"""
        pass

class Circle(Shape):
    """defines a Circle class"""
    def __init__(self, radius):
        """initilizes the radius variable"""
        self.radius = abs(radius)

    def area(self):
        """return the area"""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """return the perimeter"""
        return math.pi * self.radius * 2

class Rectangle(Shape):
    """defines a Rectangle class"""
    def __init__(self, width, height):
        """initilizes the width and height"""
        self.width = width
        self.height = height

    def area(self):
        """return the area"""
        return self.width * self.height

    def perimeter(self):
        """return the perimeter"""
        return 2 * (self.width + self.height)

def shape_info(obj):
    """prints the area and perimeter"""
    print("Area: {}".format(obj.area()))
    print("Perimeter: {}".format(obj.perimeter()))
