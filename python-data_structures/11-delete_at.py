#!/usr/bin/python3
def delete_at(my_list=[], idx=0):
    if idx >= len(my_list) or idx < 0:
        return my_list
    new_list = [0] * (len(my_list) - 1)
    d = 0
    for i in range(0, len(my_list)):
        if i != idx:
            new_list[d] = my_list[i]
            d+=1
    return new_list
