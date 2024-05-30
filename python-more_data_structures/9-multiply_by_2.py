#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new_dictionnary = {}
    for key, value in a_dictionary.items():
        new_dictionnary[key] = value * 2
    return new_dictionnary
