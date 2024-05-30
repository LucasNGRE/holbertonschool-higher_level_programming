#!/usr/bin/python3
'''module for the inherit'''


def inherits_from(obj, a_class):
    '''return true if the object is a subclass'''
    if type(obj) is not a_class:
        return issubclass(type(obj), a_class)
    return False
