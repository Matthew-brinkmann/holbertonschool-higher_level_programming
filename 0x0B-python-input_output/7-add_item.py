#!/usr/bin/python3
"""
this script adds all aguments when it is executed
to a list stored in a file add_item.json
"""
import sys
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

try:
    json_list = load_from_json_file('add_item.json')
except FileNotFoundError:
    json_list = []

for i in range(len(sys.argv)):
    if i == 0:
        continue
    json_list.append(sys.argv[i])

save_to_json_file(json_list, 'add_item.json')
