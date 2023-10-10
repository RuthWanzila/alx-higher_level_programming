#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    q = len(my_list)
    list_res = []
    for x in range(q):
        if my_list[x] % 2 == 0:
            list_res.append(True)
        else:
            list_res.append(False)
    return list_res
