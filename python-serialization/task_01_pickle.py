#!/usr/bin/python3


import pickle

class CustomObject:
    """defines a CustomObject class"""
    def __init__(self, name, age, is_student):
        """initilizes the object"""
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """displays the object"""
        print("Name: {n}\nAge: {a}\nIs Student: {s}".format(n=name, a=age, s=is_student))

    def serialize(self, filename):
        """serializes the data"""
        with open(filename, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def deserialize(cls, filename):
        """deserializes the data"""
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except Exception:
            return None
