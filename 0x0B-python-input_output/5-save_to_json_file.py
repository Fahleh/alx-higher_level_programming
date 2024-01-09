#!/usr/bin/python3
'''
    A function that writes an Object to a text file, using a JSON representation
'''
import json


def save_to_json_file(my_obj, filename):
    '''
        Accepts Python object and writes it's JSON representation to file
    '''
    with open(filename, 'w') as fd:
        fd.write(json.dumps(my_obj))
