#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    sorted_key = sorted(a_dictionary)
    new_dict = {x:a_dictionary[x] for x in sorted_key}
    print(new_dict)
