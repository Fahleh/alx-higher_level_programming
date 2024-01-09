#!/usr/bin/python3
"""
    A function that reads a text file.
"""


def read_file(filename=""):
    """Reads  UTF*a text file and prints it's content to stdout.
    Returns none
    """
    with open(filename, "r", encoding="utf-8") as fd:
        print(fd.read(), end="")
