#!/usr/bin/python3
"""appends the text to file"""


def append_write(filename="", text=""):
    """appends the file with given text"""
    with open(filename, 'a', encoding="utf-8") as f:
        k = f.write(text)
        return k
