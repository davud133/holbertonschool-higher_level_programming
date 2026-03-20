#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    import calculator_1 as calc
    if len(sys.argv) - 1 != 3:
        print("Usage: ./100-my_calculator.py <a> <operator> <b>")
        exit(1)
    else:
        a = int(sys.argv[1])
        b = int(sys.argv[3])
        if sys.argv[2] == '+':
            print("{a} + {b} = {result}".format(a=a, b=b, result=a + b))
        elif sys.argv[2] == '-':
            print("{a} - {b} = {result}".format(a=a, b=b, result=a - b))
        elif sys.argv[2] == '*':
            print("{a} * {b} = {result}".format(a=a, b=b, result=a * b))
        elif sys.argv[2] == '/':
            print("{a} / {b} = {result}".format(a=a, b=b, result=int(a / b)))
        else:
            print("Unknown operator. Available operators: +, -, * and /")
            exit(1)
