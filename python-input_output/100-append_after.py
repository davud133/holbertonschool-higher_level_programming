#!/usr/bin/python3
"""inserts a line of text to a file, after each line"""


def append_after(filename="", search_string="", new_string=""):
    """appends the new string"""
    data = ""
    with open(filename, 'r', encoding="utf-8") as f:
        data = f.read()

    pos = data.find(search_string)
    if pos == -1:
        return "String Not Found"
    pos = pos + len(search_string)
    data = data[:pos] + new_string + data[pos:]
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(data)

