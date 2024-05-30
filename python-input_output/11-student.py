#!/usr/bin/python3
'''Class to JSON'''


class Student:
    '''class student'''
    def __init__(self, first_name, last_name, age):
        '''init method for public instances attributes'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        public method that retrieves a dictionnary
        representation of a student instance
        '''
        dict = self.__dict__
        new_dict = {}
        if attrs is not None:
            for key, value in dict.items():
                if key in attrs:
                    new_dict[key] = value
            return new_dict
        return vars(self)

    def reload_from_json(self, json):
        '''Sett dynamicly attributes'''
        for key, value in json.items():
            setattr(self, key, value)
