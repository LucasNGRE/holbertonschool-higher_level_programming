#!/usr/bin/python3
'''class MyList that inherits from list'''


class MyList(list):
    '''Class MyList'''
    def print_sorted(self):
        new_list = sorted(self)
        print(new_list)
        return new_list
