#!/usr/bin/python3
"""
Module 6-max_integer
This module contains a function max_integer that finds and returns
the maximum integer in a list of integers.
"""


def max_integer(list=[]):
    """
    Returns the maximum integer in a list.

    Args:
        list (list): A list of integers or floats.

    Returns:
        int/float: The maximum number in the list, or None if list is empty.
    """
    if not list:
        return None
    return max(list)
