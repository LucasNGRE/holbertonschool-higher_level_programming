#!/usr/bin/python3
'''
function that returns the list of available
attributes and methods of an object
'''


def lookup(obj):
    '''returns the list of available attributes and method of an objects'''
    return dir(obj)
