#!/usr/bin/python3
def lookup(obj):
    """
    Returns he list of available attributes and methods of an object:
    Args:
        obj: the object

    Return:
        list: A list  of attributes an methods name
    """
    return dir(obj)
