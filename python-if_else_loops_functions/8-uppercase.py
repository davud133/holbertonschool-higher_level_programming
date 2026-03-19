#!/usr/bin/python3
def uppercase(c):
    for i in range(0, len(c)):
        print("{letter}".format(letter = chr(ord(c[i]) - 32)) if i >= 97 and i <= 122 else "{letter}".format(letter = c[i]), end="")
    print()
