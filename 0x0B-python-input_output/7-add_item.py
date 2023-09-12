#!/usr/bin/python3
import json
import sys
"""script that adds all arguments to a Python list
"""


save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file
my_file = "add_item.json"
try:
    m_list = load_from_json_file(my_file)
except FileNotFoundError:
    mf = open(my_file, "w")
    mf.write("[]")
    mf.close()
    m_list = load_from_json_file(my_file)
for e in sys.argv[1:]:
    m_list.append(e)
save_to_json_file(m_list, my_file)
