#!/usr/bin/python3
"""
3-is_kind_of_class
Module that defines the class a_class.
"""


def is_kind_of_class(obj, a_class):
    """
    Checks if an object is an instance of a class or a subclass.

     Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance of a_class, False otherwise.
    """
    if type(obj) is a_class or isinstance(obj, a_class):
        return True
    else:
        return False
