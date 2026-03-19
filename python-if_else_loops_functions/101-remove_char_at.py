#!/usr/bin/python3
def remove_char_at(str, n):
    for i in range(0, len(str)):
        if i == n:
            for d in range(n, len(str)-1):
                str[d] = str[d+1]
