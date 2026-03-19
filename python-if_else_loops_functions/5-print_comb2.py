#!/usr/bin/python3
for i in range(0, 100):
    if i < 99:
        print("{number}, ".format(number = str(i).ljust(2,'0')), end="")
    else:
        print("99")
