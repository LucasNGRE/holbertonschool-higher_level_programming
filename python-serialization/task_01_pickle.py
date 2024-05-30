#!/usr/bin/env python3
'''serialization using pickle module'''
import pickle


class CustomObject:
    '''class of custom object'''
    def __init__(self, name, age, is_student):
        '''initialize method'''
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        '''display method'''
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is student: {self.is_student}")

    def serialize(self, filename):
        '''serialize method'''
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self, f)
        except Exception as e:
            print(f"Erreur lors de la sérialisation : {e}")
            return None

    @classmethod
    def deserialize(cls, filename):
        '''deserialize method'''
        try:
            with open(filename, 'rb') as f:
                return pickle.load(f)
        except FileNotFoundError:
            print(f"Erreur : le fichier {filename} n'a pas été trouvé.")
            return None
        except Exception as e:
            print(f"Erreur lors de la désérialisation : {e}")
            return None
