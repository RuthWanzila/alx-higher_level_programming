#!/usr/bin/python3
"""
Module for MyList (inherits from list)
"""


class MyList(list):
    """
    A custom list class that contains elements of type int.
    """

    def print_sorted(self):
        """
        Prints the list in sorted order.
        """
        sorted_list = sorted(self)
        print(sorted_list)
