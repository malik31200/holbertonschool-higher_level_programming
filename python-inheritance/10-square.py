#!/usr/bin/python3
"""
7-base_geometry
Module that defines the class BaseGeometry.
"""


class BaseGeometry:
    """Represent a empty BaseGeometry class"""

    def area(self):
        """
        Calculates the area of the geometry.

        Raises:
            Exception: Indicates that area() is not implemented.
        """
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """
        Validates that a value is a positive integer.

        Args:
            name (str): The name of the parameter.
            value (int): The value to validate.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than or equal to 0.
        """
        if type(value) is not int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")


class Rectangle(BaseGeometry):
    """
    Represents a rectangle that inherits from BaseGeometry.
    """
    def __init__(self, width, height):
        """
        Initializes a rectangle with width and height.
        """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__height = height
        self.__width = width

    def area(self):
        """
        Returns the area of the rectangle
        """
        return self.__width * self.__height

    def __str__(self):
        """
        Returns a string reprensatation of the rectangle
        """
        return f"[Rectangle] {self.__width}/{self.__height}"


class Square(Rectangle):
    """
    Reprensents a square that inherits from Rectangle
    """
    def __init__(self, size):
        """
        Initializes a square with width and height.
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)
