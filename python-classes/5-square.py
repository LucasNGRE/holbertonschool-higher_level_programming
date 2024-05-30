#!/usr/bin/python3
"""This script defines a sqare class"""


class Square:
    """This is an empty class"""
    def __init__(self, size=0):
        """This is a constructor"""
        self.size = size

    @property
    def size(self):
        """Getter method for size."""
        return self.__size

    @size.setter
    def size(self, value):
        """Setter method for size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Square the size and return an int"""
        return self.__size ** 2

    def my_print(self):
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__size):
                print("#" * self.__size)
