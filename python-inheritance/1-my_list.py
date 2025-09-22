#!/usr/bin/python3
"""
1-my_list
Module that defines the class MyList
"""


class MyList(list):
    """
    A class that inherits from list
    """
    def print_sorted(self):
        """
        Prints the sorted list
        """
        list_sorted = sorted(self)
        print(list_sorted)
