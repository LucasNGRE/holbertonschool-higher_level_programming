#!/usr/bin/python3
'''module of JSON string'''
import json


def save_to_json_file(my_obj, filename):
    '''writing an object to a text file'''
    with open(filename, 'w', encoding="UTF-8") as f:
        json.dump(my_obj, f)
