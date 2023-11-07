#!/usr/bin/python3
"""
Student class with public instance attributes and a to_json method.
"""


class Student:
    """
    Class representing a student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a Student instance with the given first name,lastname,age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """
        Retrieves a dictionary representation of a Student instance.
        """
        def class_to_json(obj):
            if isinstance(obj, (list, dict, str, int, bool)):
                return obj

            if isinstance(obj, bool):
                return str(obj).lower()

            if isinstance(obj, (int, str)):
                return obj

            if isinstance(obj, dict):
                return {key: class_to_json(value)
                        for key, value in obj.items()}

            if isinstance(obj, list):
                return [class_to_json(item) for item in obj]

            attributes = {}
            for attr in obj.__dict__:
                attributes[attr] = class_to_json(obj.__dict__[attr])

            return attributes

        return class_to_json(self)
