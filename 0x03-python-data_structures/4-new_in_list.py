#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    j = len(my_list)
    duplicate = my_list.copy()
    if idx < 0 or idx > j - 1:
        return duplicate
    else:
        duplicate[idx] = element
        return duplicate
