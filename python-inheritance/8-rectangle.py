#!/usr/bin/python3
"""
8-rectangle
Module that defines the class BaseGeometry.
"""


BaseGeometry = __import__('7-base_geometry').BaseGeometry



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
