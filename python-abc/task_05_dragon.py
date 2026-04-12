#!/usr/bin/python3
"""defines mixin classes"""


class SwimMixin:
    """SwimMixin class"""
    def swim(self):
        print("The creature swims!")

class FlyMixin:
    """FlyMixin class"""
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):
    """Dragon class"""
    def roar(self):
        print("The dragon roars!")
