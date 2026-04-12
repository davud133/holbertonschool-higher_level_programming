#!/usr/bin/python3
"""defines CountedIterator class"""

class CountedIterator:
    """CountedIterator class"""
    def __init__(self, obj):
        self.iterator = iter(obj)
        self.counter = 0

    def get_count(self):
        return self.counter

    def __next__(self):
        self.counter += 1
        return next(self.iterator)
