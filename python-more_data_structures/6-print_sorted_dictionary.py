#!/usr/bin/python3
a_dictionary = {'b':1, 'a':2, 'c':3}
def print_sorted_dictionary(a_dictionary):
    sorted_key = sorted(a_dictionary)
    new_dict = {x for x in sorted_key : a_dictionary[x]}
    return new_dict
print_sorted_dictionary(a_dictionary)
