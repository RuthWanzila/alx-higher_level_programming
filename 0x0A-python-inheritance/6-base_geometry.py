#!/usr/bin/python3
"""
Module for BaseGeometry and Rectangle classes
"""


class BaseGeometry:
    """
    Base class for geometry-related operations.
    """

    def area(self):
        """
        Placeholder method for calculating the area.
        """
        raise Exception("area() is not implemented")

    def perimeter(self):
        """
        Placeholder method for calculating the perimeter.
        """
        raise Exception("perimeter() is not implemented")


class Rectangle(BaseGeometry):
    """
    Class representing a rectangle.
    """

    def __init__(self, width, height):
        """
        Initializes a Rectangle instance with the specified width and height.
        """
        self.__width = width
        self.__height = height

    def area(self):
        """
        Calculates and returns the area of the rectangle.
        """
        return self.__width * self.__height

    def perimeter(self):
        """
        Calculates and returns the perimeter of the rectangle.
        """
        return 2 * (self.__width + self.__height)
