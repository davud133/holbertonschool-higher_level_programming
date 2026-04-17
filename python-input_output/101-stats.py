#!/usr/bin/python3
"""reads stdin line by line and computes metrics"""


import sys

file_size = 0
table = {"200": 0 , "301": 0, "400": 0, "401": 0, "403": 0, "404": 0, "405": 0, "500": 0}
line_c = 0
if __name__ == "__main__":
try:
    for line in sys.stdin:
        data = line.split()
        file_size += int(data[-1])
        table[str(data[-2])]+=1
        line_c+=1
        if line_c % 10 == 0:
            print("File size: " + file_size)
            for k, v in table.items():
                print("{k}: {v}".format(k=k, v=v))
    except KeyboardInterrupt:
        print("File size: " + file_size)
        for k, v in table.items():
            print("{k}: {v}".format(k=k, v=v))
