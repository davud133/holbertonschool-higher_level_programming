#!/usr/bin/python3
"""inserts a line of text to a file, after each line"""


def append_after(filename="", search_string="", new_string=""):
    """appends the new string"""
    data = ""
    with open(filename, 'r', encoding="utf-8") as f:
        for line in f:
            pos = line.find(search_string)
            if pos == -1:
                data += line
                continue
            data = data + line + new_string
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(data)
