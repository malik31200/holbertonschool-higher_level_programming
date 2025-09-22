#!/usr/bin/python3
"""
2-is_same_class
Module that defines the class a_class.
"""


def is_same_class(obj, a_class):
    """
    Checks if an object is exactly an instance of a given class.

     Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is exactly an instance of a_class, False otherwise.
    """
    if type(obj) is a_class:
        return True
    else:
        return False
