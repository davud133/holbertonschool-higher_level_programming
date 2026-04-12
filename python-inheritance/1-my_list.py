#!/usr/bin/python3
"""defines a MyList class"""


class MyList(list):
    """defines a print_sorted method"""
    def print_sorted(self):
        print(sorted(self))
