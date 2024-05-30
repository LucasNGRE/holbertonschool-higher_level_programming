#!/usr/bin/python3
"""This script defines a sqare class"""


class Square:
    """This class represents a square"""
    def __init__(self, size=0, position=(0, 0)):
        """This is a constructor"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Getter method for size."""
        return self.__size

    @property
    def position(self):
        """Getter method for the position attribute."""
        return self.__position

    @size.setter
    def size(self, value):
        """Setter method for size with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """Setter method for the position attribute."""
        if not (isinstance(value, tuple) and len(value) == 2):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """Square the size and return an int"""
        return self.__size ** 2

    def my_print(self):
        """Print the square with the character '#'."""
        if self.__size == 0:
            print("")
        else:
            for _ in range(self.__position[1]):
                print("")
            for _ in range(self.__size):
                print(" " * self.__position[0] + "#" * self.__size)
