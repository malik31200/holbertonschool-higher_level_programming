#!/usr/bin/python3
"""
Module 11-student
class Student that defines a student
"""


class Student:
    """
    Class that defines a student.

    Attributes:
        first_name (str): The first name of the student.
        last_name (str): The last name of the student.
        age (int): The age of the student.
    """

    def __init__(self, first_name, last_name, age):
        """
        Initializes a new Student instance.

        Args:
            first_name (str): The first name of the student.
            last_name (str): The last name of the student.
            age (int): The age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """
        Retrieves a dictionary representation of the Student instance.

        Args:
            attrs (list, optional): List of attribute names to retrieve.
                If None, returns all attributes.

        Returns:
            dict: Dictionary containing the requested attributes.
        """
        if attrs is None:
            return self.__dict__.copy()

        filter_attr = {}
        for k in attrs:
            if k in self.__dict__:
                filter_attr[k] = self.__dict__[k]
        return filter_attr

    def reload_from_json(self, json):
        """
        Replaces all attributes of the Student instance.

        Args:
            json (dict): dictionary where keys are attribute and values are
            the corresponding values to update in the Student instance.
        """
        for k, v in json.items():
            setattr(self, k, v)
