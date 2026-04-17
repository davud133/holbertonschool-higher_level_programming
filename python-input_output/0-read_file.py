#!/usr/bin/python3
"""reads the text from a file"""


def read_file(filename=""):
    """reads the data of file"""
    with open(filename, 'r', encoding="utf-8") as f:
        data = f.read()
        print(data)
