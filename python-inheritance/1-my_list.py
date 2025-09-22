#!/usr/bin/python3
"""
1-my_list
Module that defines the class MyList.
"""


class MyList(list):
    """
    A class that inherits from list.

    Provides a method to print the list in ascending order.
    """
    def print_sorted(self):
        """
        Prints the list, but sorted in ascending order.

        Args:
            self: the argument.

        Returns:
            None.

        This method does not modify the original list.
        """
        list_sorted = sorted(self)
        print(list_sorted)
