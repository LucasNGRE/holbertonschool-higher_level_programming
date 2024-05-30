#!/usr/bin/python3
'''module of reading a text'''


def read_file(filename=""):
    '''read the file'''
    with open(filename, encoding="utf-8") as f:
        content = f.read()
        print(content, end="")
