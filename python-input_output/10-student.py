#!/usr/bin/python3
"""defines a Student class"""


class Student:
    """defines a Student class"""
    def __init__(self, first_name="", last_name="", age=0):
        """initilizes the Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs):
        if not isinstance(attrs, list):
            return self.__dict__
        new_dict = {}
        for i in attrs:
            new_dict[i] = self.__dict__[i]
        return new_dict
