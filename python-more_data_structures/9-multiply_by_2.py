#!/usr/bin/python3
#
#def multiply_by_2(a_dictionary):
#    new_dict = a_dictionary.copy()
#    for i, v in new_dict.items():
#        new_dict[i] = new_dict[i] * 2
#    return new_dict

def multiply_by_2(a_dictionary):
    new_dict = {x:a_dictionary[x] * 2 for x in a_dictionary.keys()}
    return new_dict
