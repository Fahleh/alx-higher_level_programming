#!/usr/bin/python3
'''
A function that returns the dictionary description with simple data structure
'''


def class_to_json(obj):
    '''A class_to_json module
       returns dictionary description with simple data structure.
    '''
    return obj.__dict__
