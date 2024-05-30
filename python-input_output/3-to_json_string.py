#!/usr/bin/python3
'''module of JSON string'''
import json


def to_json_string(my_obj):
    '''return the json representation of an object'''
    return json.dumps(my_obj)
