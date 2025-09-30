#!/usr/bin/python3
"""
Module 2-append_write
Appends a string at the end of a text file (UTF8)
Returns the number of characters added
"""


def append_write(filename="", text=""):
    """
    Function that appends a string at the end of a text file (UTF8)
    """

    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
