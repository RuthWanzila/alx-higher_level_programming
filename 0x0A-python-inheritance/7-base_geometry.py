#!/usr/bin/python3
"""
Module for the BaseGeometry class.
"""


class BaseGeometry:
    """
    Base class for geometry.
    """

    def area(self):
        """
        Raises an exception with the message "area() is not implemented".
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates the value as an integer.
        """
        if not isinstance(value, int):
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
