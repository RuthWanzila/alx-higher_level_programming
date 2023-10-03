#!/usr/bin/python3
for s in range(ord('z'), ord('a') - 1, -2):
    print("{:c}{:s}".format(s, chr(s - 33)), end="")
