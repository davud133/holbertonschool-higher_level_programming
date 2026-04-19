#!/usr/bin/python3
"""defines serialization module"""


import json

def serialize_and_save_to_file(data, filename):
    """defines a function to serialize the data"""
    with open(filename, 'w', encoding="utf-8") as f:
        f.write(json.dumps(data))

def load_and_deserialize(filename):
    """defines function to deserialize the json file"""
    with open(filename, 'r', encoding="utf-8") as f:
        data = json.loads(f.read())
        return data
