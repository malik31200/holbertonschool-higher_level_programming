#!/usr/bin/python3
"""
Module 8-class_to_json
Provides a function that returns the dictionary description
"""


def class_to_json(obj):
    """
    Args:
        obj: an instance of a class
    Returns:
        A dictionary containing all attributes of obj
    """
    return obj.__dict__.copy()
