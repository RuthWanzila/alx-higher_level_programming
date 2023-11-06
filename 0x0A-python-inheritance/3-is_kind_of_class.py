#!/usr/bin/python3
"""
Module that contains a function to check if an object is an instance of,
or if object is an instance of class that inherited from,the specified class
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of, or if the object is an instance
    of a class that inherited from, the specified class.
    Returns True if object is a kind of the specified class, False otherwise.
    """
    return isinstance(obj, a_class)
