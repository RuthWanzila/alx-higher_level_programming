#!/usr/bin/python3
def max_integer(my_list=[]):
    q = len(my_list)
    if q == 0:
        return "None"
    else:
        max_integer = my_list[0]
        for x in range(q):
            if my_list[x] > max_integer:
                max_integer = my_list[x]
        return max_integer
