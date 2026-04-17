#!/usr/bin/python3
""" script that adds all arguments to a Python list, and then save them to a file"""

save_to_json_file = __import__('5-save_to_json_file.py').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file.py').load_from_json_file
import sys
import json

my_list = []

for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])
with open(add_item.json, 'w', encoding="utf-8") as f:
    f.write(json.dumps(my_list))
