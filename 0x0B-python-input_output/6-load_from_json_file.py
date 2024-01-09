#!/usr/bin/python3
"""A function that reads a JSON file & creates a Python object from it."""
import json


def load_from_json_file(filename):
    """Create a Python object from a JSON file."""
    with open(filename) as fd:
        return json.load(fd)
