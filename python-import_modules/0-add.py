#!/usr/bin/python3
if __name__ == "__main__":
    a = 1
    b = 2
    from add_0 import add
    print("{a} + {b} = {ans}".format(a=a, b=b, ans=add(a, b)))
