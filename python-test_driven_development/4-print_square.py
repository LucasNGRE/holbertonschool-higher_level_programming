#!/usr/bin/python3
'''Function that print a square'''


def print_square(size):
    '''write a function that prints a square with the character #'''
    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise TypeError("size must be >= 0")
    if not isinstance(size, float) and size < 0:
        raise TypeError("size must be an integer")
    for _ in range(size):
        print("#" * size)
