#!/usr/bin/python3

# The shebang line above specifies the interpreter that
#should be used to execute the script (Python 3 in this case).


def class_to_json(obj):
    # Check if the object is already a serializable type
    if isinstance(obj, (list, dict, str, int, bool)):
        return obj

    # Convert boolean to lowercase string representation
    if isinstance(obj, bool):
        return str(obj).lower()

    # Return integer and string objects as is
    if isinstance(obj, (int, str)):
        return obj

    # Recursively convert dictionary objects
    if isinstance(obj, dict):
        return {key: class_to_json(value) for key, value in obj.items()}

    # Recursively convert list objects
    if isinstance(obj, list):
        return [class_to_json(item) for item in obj]

    # If obj is an instance of a custom class
    attributes = {}
    for attr in obj.__dict__:
        attributes[attr] = class_to_json(obj.__dict__[attr])

    return attributes
