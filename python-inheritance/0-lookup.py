#!/usr/bin/python3
"""
0-lookup
Module that defines the function lookup.
"""


def lookup(obj):
    """
    Returns the list of available attributes and methods of an object:
    Args:
        obj: the object

    Returns:
        list: A list  of attributes an methods names
    """
    return dir(obj)
