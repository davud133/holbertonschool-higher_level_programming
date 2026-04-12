#!/usr/bin/python3
"""defines ABC class"""

from abc import ABC, abstractmethod


class Animal(ABC):
    """defines Animal class inherited from ABC"""
    @abstractmethod
    def sound(self):
        """returns the sound of an animal"""
        pass

class Dog(Animal):
    """defines a Dog class"""
    def sound(self):
        """returns the sound of cat"""
        return "Bark"

class Cat(Animal):
    """defines a Cat class"""
    def sound(self):
        """return soudn fo cat"""
        return "Meow"
