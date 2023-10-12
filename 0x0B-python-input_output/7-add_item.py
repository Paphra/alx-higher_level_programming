#!/usr/bin/python3
"""7-add_item module

contains a script that adds all arguments to a Python list, save to a file
"""

import sys


saveJSON = __import__('5-save_to_json_file').save_to_json_file
loadJSON = __import__('6-load_from_json_file').load_from_json_file


my_list = []
filename = 'add_item.json'
if len(sys.argv) > 1:
    try:
        my_list = loadJSON(filename)
    except:
        pass
    if type(my_list) is list:
        for i in range(1, len(sys.argv)):
            my_list.append(sys.argv[i])
    else:
        my_list = []
saveJSON(my_list, filename)
