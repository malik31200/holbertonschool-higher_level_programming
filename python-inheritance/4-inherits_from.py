#!/usr/bin/python3
"""
4-inherits_from
Module that defines the functions inherits_from.
"""


def inherits_from(obj, a_class):
    """
    Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class; otherwise False.

    Args:
        obj: The object to check.
        a_class: The class to compare against.

    Returns:
        bool: True if obj is an instance,False otherwise.
    """
    return isinstance(obj, a_class) and type(obj) is not a_class
