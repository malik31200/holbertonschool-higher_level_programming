#!/usr/bin/python3
"""
6-base_geometry
Module that defines the class BaseGeometry.
"""


class BaseGeometry:
    """Class that represent a empty BaseGeometry(without attributes)"""

    def area(self):
        """
        Calculates the area of the geometry.

        aises:
            Exception: Indicates that area() is not implemented.
        """
        raise Exception("area() is not implemented")
