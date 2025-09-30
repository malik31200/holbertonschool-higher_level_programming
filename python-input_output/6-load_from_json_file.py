#!/usr/bin/python3
"""
Module 6-load_from_json_file
Provides a function that that creates an Object from a “JSON file”:
Using a JSON representation.
"""


import json


def load_from_json_file(filename):
    """
    Creates a Python object from a JSON file
    """

    with open(filename, "r", encoding="utf-8") as f:
        return json.load(f)
