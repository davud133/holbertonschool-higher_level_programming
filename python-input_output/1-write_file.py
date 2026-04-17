#!/usr/bin/python3
"""overwrites the string to the file"""


def write_file(filename="", text=""):
    """overwrites the file with the given string"""
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(text)
