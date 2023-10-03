#!/usr/bin/python3
def uppercase(str):
    for x in str:
        if ord(x) >= ord('a') and ord(x) <= ord('z'):
            char = chr(ord(x) - 32)
        else:
            char = x
        print("{:s}".format(char), end="")
    print('')
