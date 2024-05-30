#!/usr/bin/python3
"""This script defines a sqare class"""


class Square:
    """This is an empty class"""
    def __init__(self, size=0):
        """This is a constructor"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """Square the size and return an int"""
        return self.__size ** 2
