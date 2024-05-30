#!/usr/bin/python3
'''Module of the class Rectangle'''
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    '''Class square'''
    def __init__(self, size):
        '''initialization of square'''
        super().integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
