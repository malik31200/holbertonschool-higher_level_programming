#!/usr/bin/python3
"""
Module 6-square
Defines a class square with a private attribute 'size' and 'position'
Methods to compute area and print the square with "#"
"""


class Square:
    """
    Class is defines a square

    Attributes:
        __size(int): The size of a square
        __position(tuple): the (x,y) position to offset the square when printed

    Methods:
        __init__(self, size=0, position = (0,0): Initializes the Square.
        area(self): Returns the area of a square.
        my_print: print in outside a square with char # at defined position.
    """
    def __init__(self, size=0, position=(0, 0)):
        """
        Initialize a new square.

        Args:
            size(int): Size of the sqare. Default is 0.
            Position(tuple): Position (x, y) of the square(default(0,0))
        """
        self.size = size
        self.position = position

    @property
    def size(self):
        """
        Retrieve the size of the square.

        Returns:
            The current size of the square(int)
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

    @property
    def position(self):
        """
        Retrieve the position

        Returns:
            A tuple of 2 positive integers
        """
        return self.__position

    @position.setter
    def position(self, value):
        """
        Set the postion of a square with type and value to move
        Args:
            value(int): to move a square
        Raises:
            TypeError: If value is not a tuple of two integers.
            ValueError: If value < 0.
        """
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not isinstance(value[0], int) or
                not isinstance(value[1], int) or
                value[0] < 0 or value[1] < 0):
            raise TypeError("position must be a tuple of 2 positive integers")

        self.__position = value

    def area(self):
        """
        Return the area of a square.
        """
        return self.__size * self.__size

    def my_print(self):
        """
        Prints a square with "#"

        Prints an empty line in vertical position
        and space in horizental position.
        If size is 0, prints an empty line.
        """
        if self.__size == 0:
            print("")
            return

        for _ in range(self.__position[1]):
            print("")
        for _ in range(self.__size):
            print(" " * self.__position[0], "#" * self.__size)
