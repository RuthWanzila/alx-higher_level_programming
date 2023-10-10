#!/usr/bin/python3
def no_c(my_string):
    duplicate = my_string.translate({ord(i): None for i in 'cC'})
    return duplicate
