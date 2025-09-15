#!/usr/bin/python3
"""
Module 2-square
Definates a class square with a private attibutes 'size'
"""


class Square:
    """
    class is defines a square

    Attributes:
        __size (int): The size of a square

    Methods:
        __init__(self, size=0): Initializes a Square with an optional size.
    """
    def __init__(self, size=0):
        """
        Initialize a new square instance.

        Args:
            size (int, optional): The size of square in default is 0.

        Raises:
            TypeError: if the size of square is not integer.
            ValueError: if size < 0.
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
