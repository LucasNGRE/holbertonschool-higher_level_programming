#!/usr/bin/python3
'''module of writing a text'''


def write_file(filename="", text=""):
    '''return the number of character'''
    with open(filename, "w", encoding="UTF-8") as f:
        return f.write(text)
