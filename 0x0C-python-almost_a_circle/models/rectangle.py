#!/usr/bin/python3
"""
Base module that contain the first class Base
"""
from models.base import Base


class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def area(self):
        """Calculate the area of the rectangle."""
        return self.width * self.height

    def display(self):
        """Print a visual representation of the rectangle."""
        for _ in range(self.y):
            print()
        for _ in range(self.height):
            print(" " * self.x + "#" * self.width)

    def __str__(self):
        """Return a string representation of the rectangle."""
        return
    f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"

    def update(self, *args, **kwargs):
        """
        Update the attributes of the rectangle.

        Args:
            *args: variable length argument list (id, width, height, x, y)
            **kwargs: keyword arguments (id, width, height, x, y)
        """
        if args:
            attrs = ["id", "width", "height", "x", "y"]
            for i, arg in enumerate(args):
                setattr(self, attrs[i], arg)
        else:
            for key, value in kwargs.items():
                setattr(self, key, value)

    def to_dictionary(self):
        """Return a dictionary representation of the rectangle."""
        return {
            "id": self.id,
            "width": self.width,
            "height": self.height,
            "x": self.x,
            "y": self.y
        }
