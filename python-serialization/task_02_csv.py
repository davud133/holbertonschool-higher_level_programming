#!/usr/bin/python3
"""Converting CSV Data to JSON Format"""


import csv
import json

def convert_csv_to_json(filename):
    """convert_csv_to_json"""
    data = None
    try:
        with open(filename, 'r', encoding="utf-8") as f:
            data = list(csv.DictReader(f))

        with open("data.json", 'w', encoding="utf-8") as f:
            json.dump(data, f,)
        return True
    except Exception:
        return False
