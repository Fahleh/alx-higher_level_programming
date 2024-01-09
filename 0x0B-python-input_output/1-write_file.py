#!/usr/bin/python3

"""
    A function that writes a string to a text file (UTF8) &
    returns total of character written
"""


def write_file(filename="", text=""):
    """Write a string to a UTF8 text file.

    Args:
        filename (str): The name of the file to write into.
        text (str): The string to write to the file.
    Returns:
        The number of characters written.
    """
    with open(filename, 'w', encoding="utf-8") as fd:
        return fd.write(text)
