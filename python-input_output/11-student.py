#!/usr/bin/python3
"""defines a Student class"""


class Student:
    """defines a Student class"""
    def __init__(self, first_name="", last_name="", age=0):
        """initilizes the Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=0):
        if not isinstance(attrs, list):
            return self.__dict__
        new_dict = {}
        for i in attrs:
            try:
                new_dict[i] = self.__dict__[i]
            except Exception:
                continue
        return new_dict

    def reload_from_json(self, json):
        for k, v in json.items():
            self.__dict__[k] = v

