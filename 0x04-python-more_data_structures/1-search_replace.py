#!/usr/bin/python3
def search_replace(my_list, search, replace):
    result_list = [num if num != search else replace for num in my_list]
    return result_list
