#!/usr/bin/python3
def print_reversed_list_integer(my_list=[]):
    if my_list:
        j = len(my_list)
        my_list.reverse()
        for y in range(j):
            print("{:d}".format(my_list[y]))
