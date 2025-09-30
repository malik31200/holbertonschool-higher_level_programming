#!/usr/bin/python3
"""
Module 5-save_to_json_file
Provides a function that writes an Object to a text file
Using a JSON representation.
"""


import json


def save_to_json_file(my_obj, filename):
    """
    Write an object to a text file using JSON representation.

    Args:
        my_obj (any): The object to be serialized into JSON.
        filename (str): The name of the file to write the JSON string into.

    Returns:
        None
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)
