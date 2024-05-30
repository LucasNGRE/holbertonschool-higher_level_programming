#!/usr/bin/env python3
'''Module of two mixin classes'''


class SwimMixin:
    '''class swimmixin'''
    def swim(self):
        print("The creature swims!")


class FlyMixin:
    '''class flymixin'''
    def fly(self):
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    "class dragon that inherits from swimmixin and flymixin"
    def roar(self):
        print("The dragon roars!")
