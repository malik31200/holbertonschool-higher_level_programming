#!/usr/bin/python3
"""
Module 0-read_file
reads a text file (UTF8) and prints it to stdout
"""


def read_file(filename=""):
    """
    Function that reads a text file (UTF8) and prints it to stdout
    """
    with open(filename, "r", encoding="utf-8") as f:
        contenu = f.read()
        print(contenu, end="")
