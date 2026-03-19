#!/usr/bin/python3
for i in range(0, 9):
    for d in range(i + 1, 10):
        if i == 8 and d == 9:
            print("{comb}".format(comb=(str(i) + str(d))), end="\n")
        else:
            print("{comb}".format(comb=(str(i) + str(d))), end=", ")
