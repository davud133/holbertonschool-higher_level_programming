#!/usr/bin/python3
"""This module defines a function that prints a square."""


def print_square(size):
    """Prints a square with the character # of given size."""

    if type(size) is float and size < 0:
        raise TypeError("size must be an integer")

    if type(size) not in [int, float]:
        raise TypeError("size must be an integer")

    if type(size) is float:
        size = int(size)

    if size < 0:
        raise ValueError("size must be >= 0")

    for _ in range(size):
        print("#" * size)
