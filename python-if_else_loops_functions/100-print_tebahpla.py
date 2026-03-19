#!/usr/bin/python3
upper = False
for i in range(122, 96, -1):
    if upper:
        i = i - 32
        upper = False
    else:
        upper = True
    print("{letter}".format(letter=chr(i)), end="")
