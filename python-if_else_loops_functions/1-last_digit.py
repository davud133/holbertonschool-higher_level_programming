#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
num2 = number
if number < 0:
    num2 = -number
if num2 % 10 > 5:
    print(f"Last digit of {number} is {num2 % 10} and is greater than 5")
elif num2 % 10 == 0:
     print(f"Last digit of {number} is {num2 % 10} and is 0")
elif num2 % 10 < 6 and num2 % 10 != 0:
    if number < 0:
         print(f"Last digit of {number} is -{number % 10} and is less than 6 and not 0")
    else:
         print(f"Last digit of {number} is {num2 % 10} and is less than 6 and not 0")
