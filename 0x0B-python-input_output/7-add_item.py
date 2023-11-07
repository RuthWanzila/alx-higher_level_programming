#!/usr/bin/python3
"""
Script to add all arguments to a Python list and save them to a file.
"""


import sys
import json
from os.path import exists


def add_items_to_list(filename, items):
    """
    Adds items to a Python list and saves them to a file.
    """
    if exists(filename):
        with open(filename, "r") as file:
            data = json.load(file)
    else:
        data = []

    data.extend(items)

    with open(filename, "w") as file:
        json.dump(data, file)


if __name__ == "__main__":
    filename = "add_item.json"
    items = sys.argv[1:]
    add_items_to_list(filename, items)
