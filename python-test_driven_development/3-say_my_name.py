#!/usr/bin/python3
""" this module contains a functions prints the name"""


def say_my_name(first_name, last_name=""):
    """ prints the full name"""

    if not type(first_name) is str:
        raise TypeError("first_name must be a string")
    if not type(last_name) is str:
        raise TypeError("last_name must be a string")
    print("My name is {first} {last}".format(first=first_name, last=last_name))
