#!/usr/bin/python3
"""
Module 3-to_json_string
Provides a function that returns the JSON representation of an object.
"""


import json


def to_json_string(my_obj):
    """
    Convert an object to its JSON string representation.

    Args:
            my_obj (any): The object to serialize. It can be a dict, list,
                        string, int, bool, or other JSON-serializable type.

    Returns:
            str: The JSON string representation of the object.
    """

    return json.dumps(my_obj)
