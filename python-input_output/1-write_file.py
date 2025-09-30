#!/usr/bin/python3
"""
Module 1-write_file
writes a text file(UTF8) and returns the number of characters written
"""


def write_file(filename="", text=""):
    """
    Function that writes a text file(UTF8)
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
