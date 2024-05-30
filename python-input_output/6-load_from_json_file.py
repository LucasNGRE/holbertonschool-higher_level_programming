#!/usr/bin/python3
'''module of JSON string'''
import json


def load_from_json_file(filename):
    '''create an object from a json file'''
    with open(filename, 'r', encoding="UTF-8") as f:
        return json.load(f)
