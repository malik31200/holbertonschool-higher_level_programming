#!/usr/bin/python3
def uniq_add(my_list=[]):
    unique_items = set(my_list)
    result = 0
    for i in unique_items:
        result += i
    return result
