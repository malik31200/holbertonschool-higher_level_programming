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
        Prints the list, but sorted in ascending order.

        This method does not modify the original list.
        """
        list_sorted = sorted(self)
        print(list_sorted)
