#!/usr/bin/python3
'''function that returns True if the object is
exactly an instance of the specified class ; otherwise False
'''


def is_same_class(obj, a_class):
    '''Check if obj is exactly an instance of obj'''
    return type(obj) is a_class
