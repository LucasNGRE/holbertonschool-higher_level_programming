#!/usr/bin/env python3
from abc import ABC, abstractmethod
'''module for class Animal'''


class Animal(ABC):
    '''class Animal that inherits from ABC'''
    @abstractmethod
    def sound(self):
        pass


class Dog(Animal):
    '''class Dog that inherits from Animal'''
    def sound(self):
        return "Bark"


class Cat(Animal):
    '''class Cat that inherits from Animal'''
    def sound(self):
        return "Meow"
