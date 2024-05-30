#!/usr/bin/python3
'''module of writing a text'''


def append_write(filename="", text=""):
    '''append a string and return the number of character added'''
    with open(filename, "a", encoding="UTF-8") as f:
        return f.write(text)
