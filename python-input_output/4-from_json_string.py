#!/usr/bin/python3
"""
Module 4-from_json_string
Provides a function that returns an object represented by a JSON string.
"""


import json


def from_json_string(my_str):
    """
    Convert a JSON string to its corresponding Python object.

    Args:
        my_str (str): A string containing a valid JSON representation.

    Returns:
        any: The Python object represented by the JSON string
             (e.g., dict, list, str, int, bool, or None).
    """
    return json.loads(my_str)
