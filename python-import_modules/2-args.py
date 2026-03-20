#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    print("{arglen} argument".format(arglen = len(sys.argv) - 1))
    for i in range(1, len(sys.argv)):
        print("{i}: {arg}".format(i=i, arg=sys.argv[i]))
