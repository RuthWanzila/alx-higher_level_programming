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
        Initializes a Student instance with the given first name, lastname,age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of a Student instance.
        only attribute names contained in this list are retrieved.
        Otherwise, all attributes are retrieved.
        """
        if isinstance(attrs, list) and all(isinstance(attr, str)
                 for attr in attrs):
            return {attr: getattr(self, attr)
                    for attr in attrs if hasattr(self, attr)}
        return self.__dict__
