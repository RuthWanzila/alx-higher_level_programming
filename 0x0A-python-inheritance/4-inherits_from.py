#!/usr/bin/python3
"""
Module that contains function to check if class inherits from a specified class
"""


def inherits_from(obj, a_class):
    """
    Checks if a class inherits from a specified class.
    Returns True if the class inherits from the specified class,False otherwise
    """
    return issubclass(type(obj), a_class) and type(obj) != a_class
