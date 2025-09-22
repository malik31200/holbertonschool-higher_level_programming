#!/usr/bin/python3
class MyList(list):
    """
    A class hat inherits from list
    """
    def print_sorted(self):
        """
        Prints the sorted list
        """
        list_sorted = sorted(self)
        print(list_sorted)
