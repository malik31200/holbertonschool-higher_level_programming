#!/usr/bin/python3
"""
Module 0-add_integer
This module contains a function add_integer that adds two numbers
after validating and converting them to integers.
"""


def add_integer(a, b=98):
    """
    Adds two numbers after validating and converting them to integers.

    Args:
        a (int or float): The first number.
        b (int or float, optional): The second number. Default is 98.

    Returns:
        int: The sum of a and b converted to integers.

    Raises:
        TypeError: If a or b are not integers or floats.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    return int(a) + int(b)
