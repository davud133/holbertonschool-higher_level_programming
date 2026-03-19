#!/usr/bin/python3
def print_last_digit(number):
    if number < 0:
        print(-1 * number % 10, end="")
        return -1 * number % 10
    print(number % 10, end="")
    return number % 10
