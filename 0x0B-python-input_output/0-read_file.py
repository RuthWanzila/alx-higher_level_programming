#!/usr/bin/python3
"""
Module for read_file, function that reads
a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    read_file: read a file using
    with statement
    """
    with open(filename, 'r', encoding="utf-8") as f:
        print(f.read(), end="")


if __name__ == "__main__":
    file_path = 'example.txt'  # Replace with the path to your file
    read_file(file_path)
