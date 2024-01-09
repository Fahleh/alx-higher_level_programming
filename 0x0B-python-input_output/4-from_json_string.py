#!/usr/bin/python3
''' function that returns a python object represented by a JSON string
'''

import json


def from_json_string(my_str):
    ''' Accepts a JSON string representation
     returns Python objects
    '''
    return json.loads(my_str)
