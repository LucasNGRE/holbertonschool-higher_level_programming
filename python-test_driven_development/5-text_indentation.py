#!/usr/bin/python3
'''Function that indent a text after each . : or ? '''


def text_indentation(text):
    '''Indent the text'''
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    prev = False
    for char in text:
        if char == ' ' and prev:
            prev = False
            continue
        elif char in (".", "?", ":"):
            print(char)
            print()
            prev = True
        else:
            print(char, end="")
