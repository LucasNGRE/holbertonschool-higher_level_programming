#!/usr/bin/python3
'''module of JSON string'''
import json


def from_json_string(my_str):
    '''return an object by a JSON string'''
    return json.loads(my_str)
