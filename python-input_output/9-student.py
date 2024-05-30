#!/usr/bin/python3
'''Class to JSON'''


class Student:
    '''class student'''
    def __init__(self, first_name, last_name, age):
        '''init method for public instances attributes'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''
        public method that retrieves a dictionnary
        representation of a student instance
        '''
        return vars(self)
