#!/usr/bin/python3
a = 10
b = 5
if __name__ == "__main__":
    import calculator_1 as calc
    print("{a} + {b} = {ans}".format(a=a, b=b, ans=calc.add(a, b)))
    print("{a} - {b} = {ans}".format(a=a, b=b, ans=calc.sub(a, b)))
    print("{a} * {b} = {ans}".format(a=a, b=b, ans=calc.mul(a, b)))
    print("{a} / {b} = {ans}".format(a=a, b=b, ans=calc.div(a, b)))
