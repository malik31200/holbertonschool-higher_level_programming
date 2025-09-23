#!/usr/bin/python3
"""
10-square
Module that defines the class BaseGeometry.
"""


Rectangle = __import__('9-rectangle').Rectangle


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

    def area(self):
        """
        Returns the area of the square.
        """
        return self.__size ** 2
