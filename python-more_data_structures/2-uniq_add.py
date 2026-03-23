#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_set = set(my_list)
    return sum(x for x in new_set)
