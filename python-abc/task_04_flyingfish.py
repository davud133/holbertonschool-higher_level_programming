#!/usr/bin/python3
"""defines a flyingfish class"""


class Fish:
    """Fish class"""
    def swim():
        print("The fish is swimming")

    def habitat():
        print("The fish lives in water")

class Bird:
    """Bird class"""
    def fly():
        print("The bird is flying")
    def habitat():
        print("The bird lives in the sky")

class FlyingFish(Fish, Bird):
    """FlyingFish class"""
    def fly():
        print("The flying fish is soaring!")
    def swim():
        print("The flying fish is swimming!")
    def habitat():
        print("The flying fish lives both in water and the sky!")
