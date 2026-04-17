#!/usr/bin/python3
"""defines a Student class"""


class Student:
    """defines a Student class"""
    def __init__(self, first_name="", last_name="", age=0):
        """initilizes the Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        return self.__dict__
