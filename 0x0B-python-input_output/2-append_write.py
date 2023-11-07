#!/usr/bin/python3
"""
Function to append a string to the end of a text file (UTF8)
and return the number of characters added.
"""


def append_write(filename="", text=""):
    """
    Appends a string to the end of a text file
    and returns the number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as file:
        return file.write(text)
