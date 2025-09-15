#!/usr/bin/python3
"""
Module 4-square
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
        """
        self.size = size

    @property
    def size(self):
        """
        Retrieve the size of the square.
        """

        return self.__size

    @size.setter
    def size(self, value):
        """
        Set the size of a square with type and value validation
        Args:
            value(int): New size of a square
        Raises:
            TypeError: If value is not an integer.
            ValueError: If value < 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """
        Return the area of a square.
        """
        return self.__size * self.__size
