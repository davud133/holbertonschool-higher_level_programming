#!/usr/bin/python3
""" script that adds arguments to file"""


import json
import sys
save = __import__('5-save_to_json_file').save_to_json_file
load = __import__('6-load_from_json_file').load_from_json_file

my_list = []
try:
    my_list = load('add_item.json')
except Exception:
    my_list = []

for i in range(1, len(sys.argv)):
    my_list.append(sys.argv[i])
with open('add_item.json', 'w', encoding="utf-8") as f:
    f.write(json.dumps(my_list))
