#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    print("{arglen} arguments:".format(arglen=len(sys.argv) - 1) if len(sys.argv) - 1 > 1 else 
          "{arglen} argument:".format(arglen=len(sys.argv)-1) if len(sys.argv) - 1 != 0 else 
          "{arglen} arguments.".format(arglen=len(sys.argv) - 1))
    for i in range(1, len(sys.argv)):
        print("{i}: {arg}".format(i=i, arg=sys.argv[i]))
