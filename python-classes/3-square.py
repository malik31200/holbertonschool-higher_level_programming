#!/usr/bin/python3
"""
Module 3-square
Definates a class square with a private attribute 'size'
"""


class Square:
    """
    Class is defines a square

    Attributes:
        __size(int): The size of a square

    Methods:
        __init__(self, size=0): Initializes a Square with a sizea attribute.
        area(self): Returns the area of a square.
    """

    def __init__(self, size=0):
        """
        Initialize a new square instance.

        Args:
            size(int, optional): Size of the square. Default to 0.

        Raises:
            TypeError: If size is not an integer.
            ValueError: If size < 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        TReturn the area of a square.
        """
        return self.__size * self.__size
