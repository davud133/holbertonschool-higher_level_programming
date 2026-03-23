#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) is not str or roman_string is None:
        return 0
    numbers = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
    num = numbers[roman_string[0]]
    for i in range(1, len(roman_string)):
        if numbers[roman_string[i]] > numbers[roman_string[i - 1]]:
            num += numbers[roman_string[i]] - 2 * numbers[roman_string[i - 1]]
        else:
            num = num + numbers[roman_string[i]]
    return num
