#!/usr/bin/python3
"""
Function to convert a class instance into a dictionary for JSON serialization.
"""

def class_to_json(obj):
    """
    Converts an instance of a class into a dictionary for JSON serialization.
    """
    if isinstance(obj, (list, dict, str, int, bool)):
        return obj

    if isinstance(obj, bool):
        return str(obj).lower()

    if isinstance(obj, (int, str)):
        return obj

    if isinstance(obj, dict):
        return {key: class_to_json(value) for key, value in obj.items()}

    if isinstance(obj, list):
        return [class_to_json(item) for item in obj]

    attributes = {}
    for attr in obj.__dict__:
        attributes[attr] = class_to_json(obj.__dict__[attr])

    return attributes
