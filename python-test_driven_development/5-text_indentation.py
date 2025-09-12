#!/usr/bin/python3
"""
Module 5-text_indentation
Prints a text with 2 new lines after each of the characters: '.', '?', and ':'.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?' or ':'.

    Args:
        text (str): The text to print.

    Raises:
        TypeError: If text is not a string.
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    new_line_chars = ['.', '?', ':']
    current_line = ""

    for char in text:
        current_line += char
        if char in new_line_chars:
            print(current_line.strip())
            print()
            current_line = ""

    if current_line.strip():
        print(current_line.strip())
