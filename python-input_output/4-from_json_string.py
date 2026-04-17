#!/usr/bin/python3
"""decodes the json object to string"""


import json


def from_json_string(my_str):
    """decodes the json object to string"""
    return json.loads(my_str)
