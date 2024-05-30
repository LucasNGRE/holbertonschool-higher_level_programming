#!/usr/bin/env python3
'''serialization'''
import json


def serialize_and_save_to_file(data, filename):
    '''Serialize data to json format and save to a file'''
    with open(filename, 'w',) as f:
        json.dump(data, f)


def load_and_deserialize(filename):
    '''
    Load JSON data from a file and
    deserialize it into a Python dictionnary
    '''
    with open(filename, 'r',) as f:
        return json.load(f)
