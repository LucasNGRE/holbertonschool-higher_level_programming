#!/usr/bin/env python3


class CountedIterator:
    def __init__(self, obj):
        '''Initialize CountedIterator with iterator'''
        self.iter = iter(obj)
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = next(self.iter)
            self.count += 1
            return item
        except StopIteration:
            raise StopIteration

    def get_count(self):
        return self.count
