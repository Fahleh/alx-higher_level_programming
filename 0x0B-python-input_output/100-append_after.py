#!/usr/bin/python3
"""A function that inserts a line of text into a file at specified points."""


def append_after(filename="", search_string="", new_string=""):
    """Insert text after each line containing a given string in a file.
    Args:
        filename (str): Name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): String to insert.
    """
    text = ""
    with open(filename) as rd:
        for line in rd:
            text += line
            if search_string in line:
                text += new_string
    with open(filename, "w") as wr:
        wr.write(text)
