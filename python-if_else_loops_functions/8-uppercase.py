#!/usr/bin/python3
def uppercase(c):
    for i in range(0, len(c)):
        if ord(c[i]) >= 97 and ord(c[i]) <= 122:
            print("{letter}".format(letter = chr(ord(c[i]) - 32)) end="" if i != len(c) - 1 else "\n")
        else:
            print("{letter}".format(letter = c[i]), end="" if i != len(c) - 1 else "\n")

