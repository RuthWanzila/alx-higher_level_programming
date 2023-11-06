#!/usr/bin/python3
"""
Module for checking if an object is an instance of a specified class.
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of the specified class.
    Returns True if the object is an instance of the class, False otherwise.
    """
    return type(obj) is a_class
